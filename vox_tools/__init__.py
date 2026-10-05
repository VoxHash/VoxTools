"""VoxTools - A modern, cross-platform Swiss-army toolkit for developers and makers."""

__version__ = "0.2.0"
__author__ = "Silas Renner (VoxHash)"
__email__ = "contact@voxhash.dev"
__license__ = "MIT"

from vox_tools.core.plugin import PluginRegistry
from vox_tools.core.settings import Settings

__all__ = [
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "PluginRegistry",
    "Settings",
]
