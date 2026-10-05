# API Reference

API reference for VoxTools.

## Plugin Protocol

All plugins must implement the `Plugin` protocol:

```python
from vox_tools.core.plugin import Plugin
from rich.console import Console
from typing import Any, Optional
from PyQt6.QtWidgets import QWidget
from textual.app import App

class MyPlugin(Plugin):
    name: str = "my_plugin"
    summary: str = "Plugin description"
    version: str = "1.0.0"
    
    def run_cli(self, console: Console, **kwargs: Any) -> None:
        """Run plugin in CLI mode."""
        pass
    
    def tui_view(self) -> Optional[App]:
        """Return TUI app (optional)."""
        return None
    
    def gui_widget(self) -> Optional[QWidget]:
        """Return GUI widget (optional)."""
        return None
```

## Plugin Registry

```python
from vox_tools.core.plugin import registry

# Discover plugins
registry.discover_plugins()

# List plugins
plugins = registry.list_plugins()

# Get plugin
plugin = registry.get_plugin("plugin_name")

# Run plugin
registry.run_plugin_cli("plugin_name", **kwargs)
```

## Settings

```python
from vox_tools.core.settings import Settings

# Load settings
settings = Settings.load_from_file()

# Access settings
theme_mode = settings.theme.mode

# Save settings
settings.save_to_file()
```

## Theme Manager

```python
from vox_tools.core.theme import ThemeManager

theme_manager = ThemeManager()
theme = theme_manager.detect_system_theme()
colors = theme_manager.get_theme_colors(theme)
```

## See Also

- [Architecture](architecture.md)
- [CLI Reference](cli.md)
- [Examples](examples/example-01.md)
