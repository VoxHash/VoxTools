# VoxTools

[![CI](https://github.com/VoxHash/VoxTools/workflows/CI/badge.svg)](https://github.com/VoxHash/VoxTools/actions)
[![License](https://img.shields.io/github/license/VoxHash/VoxTools)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VoxHash/VoxTools?sort=semver)](https://github.com/VoxHash/VoxTools/releases)
[![Docs](https://img.shields.io/badge/docs-website-blue)](./docs/index.md)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Code style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

> A modern, cross-platform Swiss-army toolkit for developers and makers with plugin architecture, multiple interfaces (CLI/TUI/GUI), and professional tooling.

## ✨ Features
- **Multiple Interfaces**: CLI, TUI, and GUI applications
- **Plugin Architecture**: Extensible with custom plugins
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Theme Support**: System theme detection with manual switching
- **Rich Output**: Beautiful terminal output with Rich
- **Modern UI**: PyQt6 GUI with native look and feel
- **Developer Tools**: JSON/YAML formatters, regex tester, file operations, cryptography, and more

## 🧭 Table of Contents
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Examples](#-examples)
- [Architecture](#-architecture)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Quick Start
```bash
# 1) Install
pipx install voxtools
# or
pip install voxtools

# 2) Run
voxtools --help
voxtools list-plugins
voxtools tui  # Launch TUI
voxtools gui  # Launch GUI
```

## 💿 Installation
See [docs/installation.md](docs/installation.md) for platform-specific steps.

### Using pipx (Recommended)
```bash
pipx install voxtools
```

### Using Poetry
```bash
git clone https://github.com/VoxHash/VoxTools.git
cd VoxTools
poetry install
poetry run voxtools --help
```

### Using pip
```bash
pip install voxtools
```

## 🛠 Usage
Basic usage here. Advanced usage in [docs/usage.md](docs/usage.md) and [docs/cli.md](docs/cli.md).

```bash
# Core commands
voxtools version
voxtools info
voxtools list-plugins

# Launch interfaces
voxtools tui   # Terminal UI
voxtools gui   # Graphical UI
```

## ⚙️ Configuration
Configuration is stored in `~/.voxtools/config.json`. See [docs/configuration.md](docs/configuration.md) for full reference.

| Variable | Description | Default |
|---|---|---|
| `theme.mode` | Theme mode (system/light/dark) | system |
| `theme.accent_color` | Accent color in hex | #7C3AED |
| `ui.window_width` | Default window width | 1200 |
| `ui.window_height` | Default window height | 800 |
| `logging.level` | Log level | INFO |

## 📚 Examples
- Start here: [docs/examples/example-01.md](docs/examples/example-01.md)
- More: [docs/examples/](docs/examples/)

## 🧩 Architecture
VoxTools uses a plugin-based architecture with dynamic loading. See [docs/architecture.md](docs/architecture.md) for details.

**Key Components:**
- **Plugin Registry**: Auto-discovers and registers plugins
- **Core System**: Settings, theming, logging
- **Interfaces**: CLI (Typer), TUI (Textual), GUI (PyQt6)

## 🔌 Plugins

### Built-in Plugins
- **Files Plugin**: File hashing, duplicate detection, bulk operations
- **Crypto Plugin**: Hash functions, HMAC, JWT, UUID/ULID generation, Base64
- **DevTools Plugin**: JSON/YAML/TOML formatters, regex testing, .env parsing
- **Image Plugin**: AI image generation with OpenAI DALL-E

### Coming Soon
- **Media Plugin**: Audio/video conversion, thumbnails, metadata
- **Network Plugin**: Ping, DNS lookup, HTTP probing, speed testing
- **AI Plugin**: Text summarization, translation, code generation

## 🗺 Roadmap
Planned milestones live in [ROADMAP.md](ROADMAP.md). For changes, see [CHANGELOG.md](CHANGELOG.md).

## 🤝 Contributing
We welcome PRs! Please read [CONTRIBUTING.md](CONTRIBUTING.md) and follow the PR template.

## 🔒 Security
Please report vulnerabilities via [SECURITY.md](SECURITY.md).

## 📞 Support
- **Documentation**: [docs/](docs/) and [full docs](https://voxhash.github.io/VoxTools)
- **Issues**: [GitHub Issues](https://github.com/VoxHash/VoxTools/issues)
- **Contact**: See [SUPPORT.md](SUPPORT.md)

## 📄 License
This project is licensed under the terms in [LICENSE](LICENSE).

---

<div align="center">

**Made with ❤️ by [VoxHash](https://github.com/VoxHash)**

[⭐ Star this repo](https://github.com/VoxHash/VoxTools) • [🐛 Report a bug](https://github.com/VoxHash/VoxTools/issues) • [💡 Request a feature](https://github.com/VoxHash/VoxTools/issues)

</div>
