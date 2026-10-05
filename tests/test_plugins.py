"""Tests for VoxTools plugins."""


from vox_tools.core.plugin import PluginRegistry
from vox_tools.plugins.crypto.plugin import CryptoPlugin
from vox_tools.plugins.devtools.plugin import DevToolsPlugin
from vox_tools.plugins.files.plugin import FilesPlugin


class TestPluginRegistry:
    """Test the plugin registry."""

    def test_plugin_registry_creation(self):
        """Test plugin registry can be created."""
        registry = PluginRegistry()
        assert registry is not None

    def test_plugin_registration(self):
        """Test plugin registration."""
        registry = PluginRegistry()
        plugin = FilesPlugin()
        registry.register(plugin)
        assert registry.get_plugin("files") == plugin

    def test_plugin_listing(self):
        """Test plugin listing."""
        registry = PluginRegistry()
        plugin = FilesPlugin()
        registry.register(plugin)
        plugins = registry.list_plugins()
        assert len(plugins) == 1
        assert plugins[0] == plugin


class TestFilesPlugin:
    """Test the Files plugin."""

    def test_plugin_creation(self):
        """Test Files plugin can be created."""
        plugin = FilesPlugin()
        assert plugin.name == "files"
        assert plugin.summary is not None
        assert plugin.version is not None

    def test_hash_file(self, tmp_path):
        """Test file hashing."""
        plugin = FilesPlugin()
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello, World!")

        hash_result = plugin.hash_file(test_file)
        assert isinstance(hash_result, str)
        assert len(hash_result) == 64  # SHA256 hex length

    def test_find_duplicates(self, tmp_path):
        """Test duplicate file detection."""
        plugin = FilesPlugin()

        # Create duplicate files
        file1 = tmp_path / "file1.txt"
        file2 = tmp_path / "file2.txt"
        file1.write_text("Same content")
        file2.write_text("Same content")

        duplicates = plugin.find_duplicates(tmp_path)
        assert len(duplicates) == 1
        assert len(next(iter(duplicates.values()))) == 2

    def test_format_size(self):
        """Test size formatting."""
        plugin = FilesPlugin()

        assert plugin.format_size(1024) == "1.0 KB"
        assert plugin.format_size(1024 * 1024) == "1.0 MB"
        assert plugin.format_size(1024 * 1024 * 1024) == "1.0 GB"


class TestCryptoPlugin:
    """Test the Crypto plugin."""

    def test_plugin_creation(self):
        """Test Crypto plugin can be created."""
        plugin = CryptoPlugin()
        assert plugin.name == "crypto"
        assert plugin.summary is not None
        assert plugin.version is not None

    def test_hash_text(self):
        """Test text hashing."""
        plugin = CryptoPlugin()
        result = plugin.hash_text("Hello, World!")
        assert isinstance(result, str)
        assert len(result) == 64  # SHA256 hex length

    def test_generate_hmac(self):
        """Test HMAC generation."""
        plugin = CryptoPlugin()
        result = plugin.generate_hmac("Hello, World!", "secret")
        assert isinstance(result, str)
        assert len(result) == 64  # SHA256 hex length

    def test_generate_uuid(self):
        """Test UUID generation."""
        plugin = CryptoPlugin()
        result = plugin.generate_uuid()
        assert isinstance(result, str)
        assert len(result) == 36  # UUID string length

    def test_base64_encode_decode(self):
        """Test Base64 encoding and decoding."""
        plugin = CryptoPlugin()
        text = "Hello, World!"
        encoded = plugin.base64_encode(text)
        decoded = plugin.base64_decode(encoded)
        assert decoded == text


class TestDevToolsPlugin:
    """Test the DevTools plugin."""

    def test_plugin_creation(self):
        """Test DevTools plugin can be created."""
        plugin = DevToolsPlugin()
        assert plugin.name == "devtools"
        assert plugin.summary is not None
        assert plugin.version is not None

    def test_validate_json(self, tmp_path):
        """Test JSON validation."""
        plugin = DevToolsPlugin()

        # Valid JSON
        valid_json = tmp_path / "valid.json"
        valid_json.write_text('{"key": "value"}')
        result = plugin.validate_json(valid_json)
        assert result["valid"] is True

        # Invalid JSON
        invalid_json = tmp_path / "invalid.json"
        invalid_json.write_text('{"key": "value"')
        result = plugin.validate_json(invalid_json)
        assert result["valid"] is False

    def test_test_regex(self):
        """Test regex testing."""
        plugin = DevToolsPlugin()

        # Valid regex
        result = plugin.test_regex(r"\d+", "123abc456")
        assert result["valid"] is True
        assert result["match_count"] == 2

        # Invalid regex
        result = plugin.test_regex(r"[", "test")
        assert result["valid"] is False

    def test_generate_readme_badges(self):
        """Test README badge generation."""
        plugin = DevToolsPlugin()
        badges = plugin.generate_readme_badges("test-project", "test-user")
        assert "test-project" in badges
        assert "test-user" in badges
        assert "github.com" in badges
