# Quick Start

Get VoxTools running in minutes.

## Installation

```bash
# Using pipx (recommended)
pipx install voxtools

# Or using pip
pip install voxtools

# From a local clone (development)
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install -e .
```

## Basic Usage

```bash
voxtools --help
voxtools version
voxtools info
voxtools list-plugins
```

## Launch Interfaces

```bash
voxtools tui
voxtools gui
```

## Example: File Hashing

```bash
python - <<'PY'
from pathlib import Path
from vox_tools.plugins.files.plugin import FilesPlugin
print(FilesPlugin().hash_file(Path("README.md")))
PY
```

## Example: Generate UUID

```bash
python - <<'PY'
from vox_tools.plugins.crypto.plugin import CryptoPlugin
print(CryptoPlugin().generate_uuid())
PY
```

## Configuration

Defaults live in `~/.voxtools/config.json`. See [Configuration](configuration.md).

## Next Steps

- [Getting Started](getting-started.md)
- [Usage](usage.md)
- [Examples](examples/example-01.md)
