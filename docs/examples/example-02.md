# Example 2: Advanced Plugin APIs

Advanced plugin calls and configuration.

## Files: duplicates and sizing

```bash
python - <<'PY'
from pathlib import Path
from vox_tools.plugins.files.plugin import FilesPlugin

plugin = FilesPlugin()
# Point at a directory that contains intentional duplicates for a real scan
duplicates = plugin.find_duplicates(Path("."))
print(f"duplicate groups: {len(duplicates)}")
for digest, paths in list(duplicates.items())[:3]:
    print(digest[:12], len(paths))
PY
```

## Crypto: HMAC and Base64

```bash
python - <<'PY'
from vox_tools.plugins.crypto.plugin import CryptoPlugin

plugin = CryptoPlugin()
print(plugin.generate_hmac("message", "secret"))
encoded = plugin.base64_encode("Hello, World!")
print(encoded)
print(plugin.base64_decode(encoded))
PY
```

## DevTools: JSON validation and badges

```bash
python - <<'PY'
from pathlib import Path
from vox_tools.plugins.devtools.plugin import DevToolsPlugin

plugin = DevToolsPlugin()
sample = Path("/tmp/voxtools-valid.json")
sample.write_text('{"project": "VoxTools"}')
print(plugin.validate_json(sample))
print(plugin.generate_readme_badges("VoxTools", "VoxHash")[:120], "...")
PY
```

## Configuration

Edit `~/.voxtools/config.json`:

```json
{
  "theme": {
    "mode": "dark",
    "accent_color": "#7C3AED"
  },
  "ui": {
    "window_width": 1400,
    "window_height": 900
  }
}
```

Or set `VOXTOOLS_OPENAI_API_KEY` for the image plugin (requires `pip install 'voxtools[ai]'`).
