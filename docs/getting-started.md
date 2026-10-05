# Getting Started with VoxTools

Welcome to VoxTools — a cross-platform Swiss-army toolkit for developers from VoxHash Technologies.

## What is VoxTools?

VoxTools provides:

- Multiple interfaces (CLI, TUI, GUI)
- A plugin-based architecture
- Cross-platform support
- Developer utilities (files, crypto, DevTools, image)

## Installation

See [Installation](installation.md).

**Quick install:**
```bash
pipx install voxtools
```

## First Steps

1. **Verify installation:**
   ```bash
   voxtools --help
   voxtools version
   ```

2. **List available plugins:**
   ```bash
   voxtools list-plugins
   ```

3. **Try a plugin API:**
   ```bash
   python - <<'PY'
   from vox_tools.plugins.crypto.plugin import CryptoPlugin
   print(CryptoPlugin().generate_uuid())
   PY
   ```

4. **Launch the GUI or TUI:**
   ```bash
   voxtools gui
   voxtools tui
   ```

## Next Steps

- [Quick Start](quick-start.md)
- [Examples](examples/example-01.md)
- [CLI Reference](cli.md)
- [Configuration](configuration.md)

## Getting Help

- [FAQ](faq.md)
- [Troubleshooting](troubleshooting.md)
- [Support](https://github.com/VoxHash/VoxTools/issues) · contact@voxhash.dev
