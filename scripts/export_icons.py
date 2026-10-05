"""Script to export SVG logo to various icon formats."""

import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Error: PIL (Pillow) is required. Install with: pip install pillow")
    sys.exit(1)

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from vox_tools import __version__


def export_icons() -> None:
    """Export SVG logo to various icon formats."""
    # Paths
    assets_dir = project_root / "assets" / "icons"
    svg_path = assets_dir / "killer.svg"

    if not svg_path.exists():
        print(f"Error: SVG file not found at {svg_path}")
        return

    print(f"Exporting icons from {svg_path}")
    print(f"VoxTools v{__version__}")

    # Icon sizes to generate
    sizes = [16, 32, 64, 128, 256, 512, 1024]

    try:
        # Load SVG (this is a simplified approach - in production you'd use cairosvg or similar)
        # For now, we'll create a simple gradient icon programmatically
        for size in sizes:
            # Create a new image with gradient background
            img = Image.new("RGBA", (size, size), (0, 0, 0, 0))

            # Create gradient from purple to cyan
            for y in range(size):
                for x in range(size):
                    # Calculate gradient position
                    gradient_pos = (x + y) / (2 * size)

                    # Purple to cyan gradient
                    r = int(124 + (6 - 124) * gradient_pos)  # 7C -> 06
                    g = int(58 + (182 - 58) * gradient_pos)  # 3A -> B6
                    b = int(237 + (212 - 237) * gradient_pos)  # ED -> D4

                    img.putpixel((x, y), (r, g, b, 255))

            # Add a simple "K" shape (simplified)
            # This is a basic implementation - in production you'd use proper SVG rendering
            k_color = (255, 255, 255, 235)  # White with opacity

            # Draw a simple "K" shape
            k_width = size // 8
            k_height = size - size // 4
            start_x = size // 4
            start_y = size // 8

            # Vertical line
            for y in range(start_y, start_y + k_height):
                for x in range(start_x, start_x + k_width):
                    if 0 <= x < size and 0 <= y < size:
                        img.putpixel((x, y), k_color)

            # Diagonal lines
            for i in range(k_height // 2):
                # Upper diagonal
                x = start_x + k_width + i
                y = start_y + i
                if 0 <= x < size and 0 <= y < size:
                    for w in range(k_width):
                        if 0 <= x + w < size:
                            img.putpixel((x + w, y), k_color)

                # Lower diagonal
                x = start_x + k_width + i
                y = start_y + k_height - i - 1
                if 0 <= x < size and 0 <= y < size:
                    for w in range(k_width):
                        if 0 <= x + w < size:
                            img.putpixel((x + w, y), k_color)

            # Add a small circle (spark)
            spark_x = size - size // 4
            spark_y = size // 4
            spark_radius = size // 16

            for dy in range(-spark_radius, spark_radius + 1):
                for dx in range(-spark_radius, spark_radius + 1):
                    if dx * dx + dy * dy <= spark_radius * spark_radius:
                        x, y = spark_x + dx, spark_y + dy
                        if 0 <= x < size and 0 <= y < size:
                            img.putpixel((x, y), k_color)

            # Save PNG
            png_path = assets_dir / f"killer_{size}.png"
            img.save(png_path, "PNG")
            print(f"Generated {png_path}")

    except Exception as e:
        print(f"Error generating icons: {e}")
        return

    # Generate ICO file (Windows)
    try:
        ico_sizes = [16, 32, 48, 64, 128, 256]
        ico_images = []

        for size in ico_sizes:
            if size in sizes:
                png_path = assets_dir / f"killer_{size}.png"
                if png_path.exists():
                    img = Image.open(png_path)
                    ico_images.append(img)

        if ico_images:
            ico_path = assets_dir / "killer.ico"
            ico_images[0].save(
                ico_path,
                format="ICO",
                sizes=[(img.width, img.height) for img in ico_images],
            )
            print(f"Generated {ico_path}")

    except Exception as e:
        print(f"Error generating ICO: {e}")

    # Generate ICNS file (macOS) - requires icnsutil
    try:
        import subprocess

        # Check if icnsutil is available
        result = subprocess.run(
            ["icnsutil", "--help"], capture_output=True, text=True, check=False
        )
        if result.returncode == 0:
            # Create ICNS from 512x512 PNG
            png_512 = assets_dir / "killer_512.png"
            if png_512.exists():
                icns_path = assets_dir / "killer.icns"
                subprocess.run(
                    ["icnsutil", "create", str(icns_path), str(png_512)], check=True
                )
                print(f"Generated {icns_path}")
        else:
            print("icnsutil not available, skipping ICNS generation")

    except (ImportError, subprocess.CalledProcessError, FileNotFoundError):
        print("icnsutil not available, skipping ICNS generation")

    print("Icon generation complete!")


if __name__ == "__main__":
    export_icons()
