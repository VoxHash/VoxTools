"""DevTools plugin implementation."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Optional

import toml
import yaml

try:
    from PyQt6.QtWidgets import QWidget
except (ImportError, OSError):  # pragma: no cover
    QWidget = None  # type: ignore[misc, assignment]
from rich.console import Console
from textual.app import App

from vox_tools.core.plugin import Plugin


class DevToolsPlugin(Plugin):
    """Plugin for developer tools and utilities."""

    name = "devtools"
    summary = (
        "JSON/YAML/TOML formatters, regex tester, .env parser, and README generators"
    )
    version = "1.0.0"

    def run_cli(self, console: Console, **kwargs: Any) -> None:
        """Run the devtools plugin in CLI mode."""
        console.print("[bold blue]DevTools Plugin[/bold blue]")
        console.print("Available operations:")
        console.print("• format-json <file> - Format JSON file")
        console.print("• format-yaml <file> - Format YAML file")
        console.print("• format-toml <file> - Format TOML file")
        console.print("• validate-json <file> - Validate JSON file")
        console.print("• regex-test <pattern> <text> - Test regex pattern")
        console.print("• parse-env <file> - Parse .env file")
        console.print("• generate-readme - Generate README with badges")
        console.print("• track-git <directory> - Track and commit git changes")

    def tui_view(self) -> Optional[App]:
        """Return a Textual app for TUI mode."""
        return None

    def gui_widget(self) -> Optional[QWidget]:
        """Return a PyQt6 widget for GUI mode."""
        return None

    def format_json(self, file_path: Path, indent: int = 2) -> str:
        """Format JSON file."""
        try:
            with open(file_path, encoding="utf-8") as f:
                data = json.load(f)
            return json.dumps(data, indent=indent, ensure_ascii=False)
        except Exception as e:
            return f"Error formatting JSON: {e}"

    def format_yaml(self, file_path: Path) -> str:
        """Format YAML file."""
        try:
            with open(file_path, encoding="utf-8") as f:
                data = yaml.safe_load(f)
            return yaml.dump(data, default_flow_style=False, sort_keys=False)
        except Exception as e:
            return f"Error formatting YAML: {e}"

    def format_toml(self, file_path: Path) -> str:
        """Format TOML file."""
        try:
            with open(file_path, encoding="utf-8") as f:
                data = toml.load(f)
            return toml.dumps(data)
        except Exception as e:
            return f"Error formatting TOML: {e}"

    def validate_json(self, file_path: Path) -> dict[str, Any]:
        """Validate JSON file."""
        try:
            with open(file_path, encoding="utf-8") as f:
                json.load(f)
            return {"valid": True, "error": None}
        except Exception as e:
            return {"valid": False, "error": str(e)}

    def test_regex(self, pattern: str, text: str) -> dict[str, Any]:
        """Test regex pattern against text."""
        try:
            regex = re.compile(pattern)
            matches = regex.findall(text)
            return {
                "valid": True,
                "matches": matches,
                "match_count": len(matches),
                "error": None,
            }
        except Exception as e:
            return {"valid": False, "matches": [], "match_count": 0, "error": str(e)}

    def parse_env_file(self, file_path: Path) -> dict[str, str]:
        """Parse .env file."""
        env_vars = {}
        try:
            with open(file_path, encoding="utf-8") as f:
                for _line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if line and not line.startswith("#"):
                        if "=" in line:
                            key, value = line.split("=", 1)
                            env_vars[key.strip()] = value.strip()
                        # Silently skip invalid lines (no warning needed for parsing)
        except Exception:
            # Return empty dict on error - caller can handle logging if needed
            pass
        return env_vars

    def generate_readme_badges(self, project_name: str, github_user: str) -> str:
        """Generate README badges for a project."""
        badges = [
            f"[![CI](https://github.com/{github_user}/{project_name}/workflows/CI/badge.svg)](https://github.com/{github_user}/{project_name}/actions)",
            f"[![Coverage](https://codecov.io/gh/{github_user}/{project_name}/branch/main/graph/badge.svg)](https://codecov.io/gh/{github_user}/{project_name})",
            "[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)",
            "[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)",
            "[![Code style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)",
        ]
        return "\n".join(badges)

    def track_git_changes(
        self,
        directory: Path,
        commit_message: str = "Update tracked files",
        auto_push: bool = False,
    ) -> dict[str, Any]:
        """Track and commit all git changes in a repository."""
        import subprocess

        result = {
            "success": False,
            "committed": False,
            "pushed": False,
            "message": "",
            "errors": [],
        }

        try:
            # Check if directory is a git repository
            git_dir = directory / ".git"
            if not git_dir.exists():
                result["message"] = "Not a git repository"
                return result

            # Check for uncommitted changes
            status_result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=directory,
                capture_output=True,
                text=True,
                check=False,
            )

            if status_result.stdout.strip():
                # Stage all changes
                subprocess.run(
                    ["git", "add", "-A"],
                    cwd=directory,
                    check=True,
                    capture_output=True,
                )

                # Commit changes
                subprocess.run(
                    ["git", "commit", "-m", commit_message],
                    cwd=directory,
                    check=True,
                    capture_output=True,
                )

                result["committed"] = True
                result["message"] = "Changes committed successfully"

                # Check if local is ahead of remote
                subprocess.run(
                    ["git", "fetch", "origin"],
                    cwd=directory,
                    check=False,
                    capture_output=True,
                )

                local_commits_result = subprocess.run(
                    ["git", "log", "origin/main..HEAD", "--oneline"],
                    cwd=directory,
                    capture_output=True,
                    text=True,
                    check=False,
                )

                if local_commits_result.stdout.strip() and auto_push:
                    # Push to remote
                    subprocess.run(
                        ["git", "push", "origin", "main"],
                        cwd=directory,
                        check=True,
                        capture_output=True,
                    )
                    result["pushed"] = True
                    result["message"] += " and pushed to remote"

            else:
                result["message"] = "No uncommitted changes found"

            result["success"] = True

        except subprocess.CalledProcessError as e:
            result["errors"].append(
                f"Git command failed: {e.stderr.decode() if e.stderr else str(e)}"
            )
            result["message"] = "Failed to track git changes"
        except Exception as e:
            result["errors"].append(str(e))
            result["message"] = f"Error: {e!s}"

        return result


# Create plugin instance
plugin = DevToolsPlugin()
