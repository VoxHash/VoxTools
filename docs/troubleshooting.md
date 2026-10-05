# Troubleshooting

Common issues and solutions.

## Installation Issues

### Module Not Found
**Problem**: `ModuleNotFoundError` when running commands.

**Solution**: Ensure all dependencies are installed:
```bash
pip install --upgrade voxtools
# or
poetry install
```

### Permission Denied
**Problem**: Permission errors on installation.

**Solution**: Use `pipx` or virtual environment:
```bash
pipx install voxtools
```

## Runtime Issues

### Plugin Not Found
**Problem**: Plugin not discovered.

**Solution**: 
- Check plugin is in `vox_tools/plugins/`
- Verify plugin has `plugin` instance
- Run `voxtools list-plugins` to verify

### GUI Not Launching
**Problem**: GUI fails to start.

**Solution**:
- Check PyQt6 is installed: `pip install PyQt6`
- Verify display configuration (Linux)
- Check system requirements

### `voxtools --help` crashes with `make_metavar() missing … ctx`
**Problem**: Old Typer + new Click incompatibility.

**Solution**: Upgrade to VoxTools 0.2.0+ (`typer>=0.16`). Reinstall:
```bash
pip install -U 'voxtools>=0.2.0'
```

### Still seeing KillerTools / killertools
**Problem**: Leftover install or docs after the rename.

**Solution**: Install `voxtools`. The `killertools` command remains as a legacy alias to the same app.

## Configuration Issues

### Settings Not Saving
**Problem**: Settings not persisting.

**Solution**:
- Check `~/.voxtools/` directory permissions
- Verify JSON syntax in config file
- Check disk space

## Getting More Help

- [FAQ](faq.md)
- [GitHub Issues](https://github.com/VoxHash/VoxTools/issues)
- [Support](https://github.com/VoxHash/VoxTools/discussions)
