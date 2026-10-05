# Architecture

High-level architecture of VoxTools.

## Overview

VoxTools uses a plugin-based architecture with multiple interfaces.

## Core Components

### Plugin System
- **Plugin Registry**: Auto-discovers and registers plugins
- **Plugin Protocol**: Standard interface for all plugins
- **Dynamic Loading**: Plugins loaded at runtime

### Interfaces
- **CLI**: Typer-based command-line interface
- **TUI**: Textual-based terminal user interface
- **GUI**: PyQt6-based graphical user interface

### Core Services
- **Settings Management**: Pydantic-based configuration
- **Theme System**: Cross-platform theme detection and application
- **Logging System**: Rich console and file logging

## Plugin Architecture

```
vox_tools/
├── core/
│   ├── plugin.py      # Plugin protocol and registry
│   ├── settings.py    # Settings management
│   ├── theme.py       # Theme management
│   └── logging.py     # Logging system
└── plugins/
    ├── files/         # Files plugin
    ├── crypto/        # Crypto plugin
    └── devtools/      # DevTools plugin
```

## Data Flow

1. User invokes command
2. CLI/TUI/GUI routes to plugin
3. Plugin executes functionality
4. Results returned to interface
5. Interface displays results

## See Also

- [Plugin Development](creating-plugins.md)
- [API Reference](api.md)
