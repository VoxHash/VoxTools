# FAQ

Frequently asked questions about VoxTools.

## General

### What is VoxTools?
VoxTools is a modern, cross-platform Swiss-army toolkit for developers and makers with plugin architecture and multiple interfaces.

### What platforms are supported?
Windows, macOS, and Linux.

### How do I install VoxTools?
See [Installation Guide](installation.md).

## Plugins

### How do I create a plugin?
Implement the `Plugin` protocol in `vox_tools/plugins/<name>/plugin.py` and expose a `plugin` instance. See [Architecture](architecture.md) and [API](api.md).

### Was this project renamed?
Yes. KillerTools was renamed to **VoxTools** in 0.2.0. The `killertools` CLI alias and `~/.killertools/config.json` fallback remain for migration.

### Can I install third-party plugins?
Plugin marketplace coming soon. For now, plugins must be in the `vox_tools/plugins/` directory.

### How do plugins work?
Plugins are auto-discovered and registered. They implement the Plugin protocol.

## Usage

### How do I change the theme?
Use the theme setting in configuration or `--theme` option.

### Can I use multiple interfaces?
Yes, you can use CLI, TUI, and GUI independently.

### How do I configure settings?
Edit `~/.voxtools/config.json` or use environment variables.

## Development

### How do I contribute?
See [Contributing Guide](../CONTRIBUTING.md).

### What's the development setup?
See [Contributing Guide](../CONTRIBUTING.md).

## Support

### Where can I get help?
- [Documentation](index.md)
- [GitHub Issues](https://github.com/VoxHash/VoxTools/issues)
- [Support Guide](../SUPPORT.md)
