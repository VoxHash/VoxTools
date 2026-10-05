# Example 1: Basic Plugin Usage

Use VoxTools plugins from the CLI discovery path and Python APIs.

## List Plugins

```bash
voxtools list-plugins
```

## Files plugin (hash a file)

```bash
python - <<'PY'
from pathlib import Path
from vox_tools.plugins.files.plugin import FilesPlugin

plugin = FilesPlugin()
print(plugin.hash_file(Path("README.md")))
print(plugin.format_size(Path("README.md").stat().st_size))
PY
```

## Crypto plugin

```bash
python - <<'PY'
from vox_tools.plugins.crypto.plugin import CryptoPlugin

plugin = CryptoPlugin()
print(plugin.generate_uuid())
print(plugin.hash_text("Hello, World!"))
print(plugin.base64_encode("Hello, World!"))
PY
```

## DevTools plugin

```bash
python - <<'PY'
from pathlib import Path
from vox_tools.plugins.devtools.plugin import DevToolsPlugin

plugin = DevToolsPlugin()
print(plugin.test_regex(r"\d+", "123abc456"))
readme = Path("README.md")
if readme.exists():
    # Validate JSON only when you have a JSON file:
    sample = Path("/tmp/voxtools-sample.json")
    sample.write_text('{"ok": true}')
    print(plugin.validate_json(sample))
PY
```

## Launch GUI

```bash
voxtools gui
```

Then select a plugin from the sidebar.
