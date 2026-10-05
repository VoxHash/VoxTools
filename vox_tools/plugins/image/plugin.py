"""Image generator plugin implementation."""

from __future__ import annotations

import os
from io import BytesIO
from pathlib import Path
from typing import Any, Optional

from PIL import Image
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import (
    QComboBox,
    QFileDialog,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from rich.console import Console
from textual.app import App

try:
    import openai
except ImportError:
    openai = None  # type: ignore

from vox_tools.core.plugin import Plugin


class ImageGeneratorPlugin(Plugin):
    """Plugin for AI image generation using OpenAI DALL-E."""

    name = "image"
    summary = (
        "AI image generation using OpenAI DALL-E with customizable filters and styles"
    )
    version = "1.0.0"

    def __init__(self) -> None:
        """Initialize the image generator plugin."""
        self.api_key: Optional[str] = None
        self._load_api_key()

    def _load_api_key(self) -> None:
        """Load OpenAI API key from environment or config."""
        # Try environment variable first
        self.api_key = os.getenv("OPENAI_API_KEY")

        # If not found, try to load from a config file
        if not self.api_key:
            config_path = Path.home() / ".voxtools" / "openai_key.txt"
            if config_path.exists():
                try:
                    self.api_key = config_path.read_text().strip()
                except Exception:
                    pass

    def run_cli(self, console: Console, **kwargs: Any) -> None:
        """Run the image generator plugin in CLI mode."""
        console.print("[bold blue]Image Generator Plugin[/bold blue]")
        console.print("\n[bold]Usage:[/bold]")
        console.print(
            "  voxtools image generate --prompt 'your prompt' [--filter FILTER] [--size SIZE]"
        )
        console.print("\n[bold]Options:[/bold]")
        console.print("  --prompt, -p    : Image generation prompt (required)")
        console.print(
            "  --filter, -f    : Filter style (None, Anime, Cyberpunk) [default: None]"
        )
        console.print("  --size, -s      : Image size (256, 512, 1024) [default: 512]")
        console.print(
            "  --output, -o    : Output file path [default: generated_image.png]"
        )
        console.print(
            "  --api-key, -k   : OpenAI API key (or set OPENAI_API_KEY env var)"
        )
        console.print("\n[bold]Examples:[/bold]")
        console.print("  voxtools image generate -p 'a sunset over mountains'")
        console.print("  voxtools image generate -p 'a cat' -f Anime -s 1024")

        if not openai:
            console.print(
                "\n[yellow]Warning:[/yellow] openai package not installed. Install with: pip install openai"
            )
        elif not self.api_key:
            console.print(
                "\n[yellow]Warning:[/yellow] OpenAI API key not found. Set OPENAI_API_KEY or use --api-key"
            )

    def tui_view(self) -> Optional[App]:
        """Return a Textual app for TUI mode."""
        return None  # TUI not implemented yet

    def gui_widget(self) -> Optional[QWidget]:
        """Return a PyQt6 widget for GUI mode."""
        return ImageGeneratorWidget(self)

    def generate_image(
        self,
        prompt: str,
        filter_type: str = "None",
        size: str = "512",
        api_key: Optional[str] = None,
    ) -> Optional[Image.Image]:
        """Generate an image using OpenAI DALL-E."""
        if not openai:
            raise ImportError(
                "openai package is required. Install with: pip install openai"
            )

        # Use provided API key or fall back to instance key
        key = api_key or self.api_key
        if not key:
            raise ValueError(
                "OpenAI API key is required. Set OPENAI_API_KEY environment variable "
                "or provide --api-key argument"
            )

        openai.api_key = key

        # Build the prompt with filter
        full_prompt = prompt
        if filter_type and filter_type != "None":
            full_prompt = f"{prompt} with {filter_type} filter"

        try:
            # Use the newer OpenAI client API if available
            try:
                from openai import OpenAI

                client = OpenAI(api_key=key)
                response = client.images.generate(
                    model="dall-e-2",
                    prompt=full_prompt,
                    n=1,
                    size=f"{size}x{size}",
                )
                image_url = response.data[0].url
            except (AttributeError, ImportError):
                # Fallback to older API
                response = openai.Image.create(
                    prompt=full_prompt,
                    n=1,
                    size=f"{size}x{size}",
                )
                image_url = response["data"][0]["url"]

            # Download and convert to PIL Image
            import requests

            image_data = requests.get(image_url).content
            return Image.open(BytesIO(image_data))

        except Exception as e:
            raise RuntimeError(f"Failed to generate image: {e}") from e

    def save_image(self, image: Image.Image, file_path: Path) -> None:
        """Save an image to a file."""
        image.save(file_path)


class ImageGeneratorWidget(QWidget):
    """GUI widget for image generation."""

    def __init__(self, plugin: ImageGeneratorPlugin) -> None:
        """Initialize the image generator widget."""
        super().__init__()
        self.plugin = plugin
        self.generated_image: Optional[QPixmap] = None
        self._setup_ui()

    def _setup_ui(self) -> None:
        """Set up the user interface."""
        layout = QVBoxLayout()

        # Title
        title = QLabel("AI Image Generator")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        # API Key input (if not set)
        if not self.plugin.api_key:
            api_key_label = QLabel("OpenAI API Key:")
            layout.addWidget(api_key_label)
            self.api_key_input = QLineEdit()
            self.api_key_input.setPlaceholderText("Enter your OpenAI API key...")
            self.api_key_input.setEchoMode(QLineEdit.EchoMode.Password)
            layout.addWidget(self.api_key_input)
        else:
            self.api_key_input = None

        # Prompt input
        prompt_label = QLabel("Prompt:")
        layout.addWidget(prompt_label)
        self.prompt_input = QLineEdit()
        self.prompt_input.setPlaceholderText("Enter your prompt here...")
        layout.addWidget(self.prompt_input)

        # Filter selection
        filter_label = QLabel("Filter:")
        layout.addWidget(filter_label)
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["None", "Anime", "Cyberpunk"])
        layout.addWidget(self.filter_combo)

        # Size selection
        size_label = QLabel("Size:")
        layout.addWidget(size_label)
        self.size_combo = QComboBox()
        self.size_combo.addItems(["256", "512", "1024"])
        self.size_combo.setCurrentText("512")
        layout.addWidget(self.size_combo)

        # Generate button
        self.generate_button = QPushButton("Generate Image")
        self.generate_button.clicked.connect(self._generate_image)
        layout.addWidget(self.generate_button)

        # Save button
        self.save_button = QPushButton("Save Image")
        self.save_button.clicked.connect(self._save_image)
        self.save_button.setEnabled(False)
        layout.addWidget(self.save_button)

        # Image display
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setMinimumHeight(300)
        self.image_label.setStyleSheet(
            "border: 1px solid gray; background-color: #f0f0f0;"
        )
        layout.addWidget(self.image_label)

        self.setLayout(layout)

    def _generate_image(self) -> None:
        """Generate an image based on user input."""
        prompt = self.prompt_input.text().strip()
        if not prompt:
            QMessageBox.warning(self, "Input Error", "Please enter a prompt.")
            return

        # Get API key
        api_key = None
        if self.api_key_input:
            api_key = self.api_key_input.text().strip()
            if not api_key:
                QMessageBox.warning(
                    self, "API Key Required", "Please enter your OpenAI API key."
                )
                return

        filter_type = self.filter_combo.currentText()
        size = self.size_combo.currentText()

        try:
            self.generate_button.setEnabled(False)
            self.generate_button.setText("Generating...")

            # Generate image
            pil_image = self.plugin.generate_image(
                prompt=prompt,
                filter_type=filter_type,
                size=size,
                api_key=api_key,
            )

            if pil_image:
                # Convert PIL Image to QPixmap
                q_image = QImage(
                    pil_image.tobytes(),
                    pil_image.width,
                    pil_image.height,
                    pil_image.width * 3,
                    QImage.Format.Format_RGB888,
                )
                pixmap = QPixmap.fromImage(q_image)
                self.generated_image = pixmap
                self.image_label.setPixmap(
                    pixmap.scaled(
                        self.image_label.size(),
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation,
                    )
                )
                self.save_button.setEnabled(True)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to generate image:\n{e!s}")
        finally:
            self.generate_button.setEnabled(True)
            self.generate_button.setText("Generate Image")

    def _save_image(self) -> None:
        """Save the generated image to a file."""
        if not self.generated_image:
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Image",
            "",
            "PNG Files (*.png);;JPEG Files (*.jpg);;All Files (*)",
        )

        if file_path:
            try:
                self.generated_image.save(file_path)
                QMessageBox.information(self, "Success", "Image saved successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save image:\n{e!s}")


# Create plugin instance
plugin = ImageGeneratorPlugin()
