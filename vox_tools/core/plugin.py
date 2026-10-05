"""Plugin architecture for VoxTools."""

from __future__ import annotations

import importlib
import pkgutil
from abc import abstractmethod
from pathlib import Path
from typing import Any, Optional, Protocol, runtime_checkable

from rich.console import Console

# Optional GUI/TUI imports - handle gracefully if not available
try:
    from textual.app import App
except ImportError:
    App = None  # type: ignore

try:
    from PyQt6.QtWidgets import QWidget
except ImportError:
    QWidget = None  # type: ignore


@runtime_checkable
class Plugin(Protocol):
    """Protocol defining the interface for VoxTools plugins."""

    name: str
    """The plugin name."""

    summary: str
    """A brief description of what the plugin does."""

    version: str
    """The plugin version."""

    @abstractmethod
    def run_cli(self, console: Console, **kwargs: Any) -> None:
        """Run the plugin in CLI mode."""
        ...

    def tui_view(self) -> Optional[Any]:
        """Return a Textual app for TUI mode. Optional."""
        return None

    def gui_widget(self) -> Optional[Any]:
        """Return a PyQt6 widget for GUI mode. Optional."""
        return None


class PluginRegistry:
    """Registry for managing VoxTools plugins."""

    def __init__(self) -> None:
        """Initialize the plugin registry."""
        self._plugins: dict[str, Plugin] = {}
        self._console = Console()

    def register(self, plugin: Plugin) -> None:
        """Register a plugin."""
        if plugin.name in self._plugins:
            self._console.print(
                f"[yellow]Warning: Plugin '{plugin.name}' is already registered[/yellow]"
            )
            return

        self._plugins[plugin.name] = plugin
        self._console.print(
            f"[green]Registered plugin: {plugin.name} v{plugin.version}[/green]"
        )

    def get_plugin(self, name: str) -> Optional[Plugin]:
        """Get a plugin by name."""
        return self._plugins.get(name)

    def list_plugins(self) -> list[Plugin]:
        """List all registered plugins."""
        return list(self._plugins.values())

    def discover_plugins(self) -> None:
        """Auto-discover and register plugins from the plugins package."""
        plugins_package = "vox_tools.plugins"

        try:
            package = importlib.import_module(plugins_package)
            package_path = Path(package.__file__).parent  # type: ignore

            for _finder, name, ispkg in pkgutil.iter_modules([str(package_path)]):
                if ispkg:
                    module_name = f"{plugins_package}.{name}.plugin"
                    try:
                        module = importlib.import_module(module_name)

                        # First, check for a plugin instance (most common pattern)
                        if hasattr(module, "plugin"):
                            plugin_instance = module.plugin
                            if isinstance(plugin_instance, Plugin):
                                self.register(plugin_instance)
                                continue

                        # Fallback: Look for plugin classes
                        for attr_name in dir(module):
                            attr = getattr(module, attr_name)
                            if (
                                isinstance(attr, type)
                                and hasattr(attr, "name")
                                and hasattr(attr, "summary")
                                and hasattr(attr, "version")
                                and hasattr(attr, "run_cli")
                                and not attr_name.startswith("_")
                                and attr_name.endswith("Plugin")
                            ):
                                try:
                                    plugin_instance = attr()
                                    if isinstance(plugin_instance, Plugin):
                                        self.register(plugin_instance)
                                        self._console.print(
                                            f"Registered plugin: {plugin_instance.name} v{plugin_instance.version}"
                                        )
                                        break  # Only register one plugin per module
                                except Exception as e:
                                    self._console.print(
                                        f"[red]Failed to instantiate plugin {attr_name}: {e}[/red]"
                                    )

                    except ImportError as e:
                        # Silently skip plugins with missing optional dependencies
                        self._console.print(
                            f"[yellow]Skipping plugin {module_name}: {e}[/yellow]"
                        )
                    except Exception as e:
                        self._console.print(
                            f"[red]Failed to import plugin module {module_name}: {e}[/red]"
                        )

        except Exception as e:
            self._console.print(f"[red]Failed to discover plugins: {e}[/red]")

    def run_plugin_cli(self, name: str, **kwargs: Any) -> bool:
        """Run a plugin in CLI mode."""
        plugin = self.get_plugin(name)
        if not plugin:
            self._console.print(f"[red]Plugin '{name}' not found[/red]")
            return False

        try:
            plugin.run_cli(self._console, **kwargs)
            return True
        except Exception as e:
            self._console.print(f"[red]Error running plugin '{name}': {e}[/red]")
            return False


# Global plugin registry instance
registry = PluginRegistry()
