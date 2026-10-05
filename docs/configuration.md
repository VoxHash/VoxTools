# Configuration

Configure VoxTools to your preferences.

## Configuration File

Settings are stored in `~/.voxtools/config.json`.

If that file is missing, VoxTools will also read a legacy `~/.killertools/config.json` from the previous KillerTools brand name. New saves always write to `~/.voxtools/`.

## Settings

### Theme
```json
{
  "theme": {
    "mode": "system",
    "accent_color": "#7C3AED",
    "font_family": "system"
  }
}
```

**Theme modes:**
- `system` — detect OS theme
- `light` — force light theme
- `dark` — force dark theme

### UI Settings
```json
{
  "ui": {
    "window_width": 1200,
    "window_height": 800,
    "sidebar_width": 250,
    "show_tooltips": true,
    "animations": true
  }
}
```

### Logging
```json
{
  "logging": {
    "level": "INFO",
    "file_logging": true,
    "max_file_size": 10,
    "backup_count": 5
  }
}
```

## Environment Variables

All settings use the `VOXTOOLS_` prefix (via pydantic-settings). Common values:

| Variable | Purpose |
| --- | --- |
| `VOXTOOLS_OPENAI_API_KEY` | OpenAI key for the image (and future AI) plugins |
| `VOXTOOLS_IMGBB_API_KEY` | ImgBB upload key (optional) |
| `VOXTOOLS_TELEGRAM_BOT_TOKEN` | Telegram bot token (optional) |
| `VOXTOOLS_FFMPEG_PATH` | Path to an FFmpeg binary for media workflows |
| `VOXTOOLS_THEME_MODE` | Override theme mode (`system` / `light` / `dark`) |

System dependencies (not env vars): Python 3.11–3.13, optional FFmpeg for media, GUI display/Qt libs for `voxtools gui`.

## Plugin Settings

Plugin-specific settings live under `plugin_settings`:

```json
{
  "plugin_settings": {
    "files": {
      "default_hash": "sha256"
    }
  }
}
```

## See Also

- [Usage Guide](usage.md)
- [CLI Reference](cli.md)
