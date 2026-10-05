# CLI Reference

Command-line interface for VoxTools (Typer + Rich).

## Global Commands

| Command | Description |
| --- | --- |
| `voxtools --help` | Show help |
| `voxtools version` | Print version |
| `voxtools info` | Product overview and quick tips |
| `voxtools list-plugins` | Discover and list registered plugins |
| `voxtools tui` | Launch the Textual TUI |
| `voxtools gui` | Launch the PyQt6 GUI |

Legacy install alias: `killertools` runs the same entry point as `voxtools`.

## Plugin usage today

Plugins are discovered via `voxtools list-plugins` and used from Python (and the TUI/GUI shells). Dedicated `voxtools <plugin> …` Typer subcommands are on the [roadmap](../ROADMAP.md).

```bash
# Inspect what is loaded
voxtools list-plugins

# Programmatic example (files hash)
python - <<'PY'
from pathlib import Path
from vox_tools.plugins.files.plugin import FilesPlugin
print(FilesPlugin().hash_file(Path("README.md")))
PY
```

```bash
# Crypto helpers
python - <<'PY'
from vox_tools.plugins.crypto.plugin import CryptoPlugin
p = CryptoPlugin()
print(p.generate_uuid())
print(p.hash_text("hello"))
PY
```

```bash
# DevTools helpers
python - <<'PY'
from vox_tools.plugins.devtools.plugin import DevToolsPlugin
print(DevToolsPlugin().test_regex(r"\d+", "abc123"))
PY
```

## Environment

See [Configuration](configuration.md) for `VOXTOOLS_*` variables and config paths.

## See Also

- [Usage Guide](usage.md)
- [Examples](examples/example-01.md)
