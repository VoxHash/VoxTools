"""Core functionality for VoxTools."""

from vox_tools.core.logging import setup_logging
from vox_tools.core.plugin import Plugin, PluginRegistry
from vox_tools.core.settings import Settings
from vox_tools.core.theme import ThemeManager

__all__ = ["Plugin", "PluginRegistry", "Settings", "ThemeManager", "setup_logging"]
