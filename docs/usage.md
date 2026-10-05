# Usage Guide

How to run VoxTools day to day.

## Command Structure

```bash
voxtools [command]
```

## Core Commands

```bash
voxtools version
voxtools info
voxtools list-plugins
voxtools tui    # Terminal UI
voxtools gui    # Graphical UI
```

## Working with plugins

1. List discovered plugins:

```bash
voxtools list-plugins
```

2. Call plugin APIs from Python (current stable interface):

```python
from pathlib import Path
from vox_tools.plugins.files.plugin import FilesPlugin
from vox_tools.plugins.crypto.plugin import CryptoPlugin
from vox_tools.plugins.devtools.plugin import DevToolsPlugin

print(FilesPlugin().hash_file(Path("README.md")))
print(CryptoPlugin().generate_uuid())
print(DevToolsPlugin().test_regex(r"\w+", "hello world"))
```

3. Or open `voxtools tui` / `voxtools gui` for interactive use.

Dedicated CLI subcommands per plugin are planned; see [ROADMAP.md](../ROADMAP.md).

## Configuration

See [Configuration](configuration.md). Defaults live in `~/.voxtools/config.json`.

## Image plugin notes

The image plugin needs `VOXTOOLS_OPENAI_API_KEY` (or a configured key in settings) and the optional `ai` extra:

```bash
pip install 'voxtools[ai]'
```

## Advanced

- [CLI Reference](cli.md)
- [Examples](examples/example-01.md)
- [Architecture](architecture.md)
