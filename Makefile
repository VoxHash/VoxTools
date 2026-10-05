# VoxTools Makefile
# Cross-platform build and development commands

.PHONY: help setup install dev test lint format typecheck build clean run-cli run-tui run-gui icons

# Default target
help:
	@echo "VoxTools - Available commands:"
	@echo ""
	@echo "Setup & Development:"
	@echo "  setup          - Set up development environment"
	@echo "  install        - Install dependencies"
	@echo "  dev            - Install development dependencies"
	@echo ""
	@echo "Code Quality:"
	@echo "  test           - Run tests"
	@echo "  lint           - Run linters (Ruff)"
	@echo "  format         - Format code (Black, isort)"
	@echo "  typecheck      - Run type checker (mypy)"
	@echo "  quality        - Run all quality checks"
	@echo ""
	@echo "Building:"
	@echo "  build          - Build wheels and binaries"
	@echo "  icons          - Generate icon files"
	@echo "  clean          - Clean build artifacts"
	@echo ""
	@echo "Running:"
	@echo "  run-cli        - Run CLI application"
	@echo "  run-tui        - Run TUI application"
	@echo "  run-gui        - Run GUI application"
	@echo ""

# Setup development environment
setup: install dev
	@echo "Setting up pre-commit hooks..."
	poetry run pre-commit install
	@echo "Development environment ready!"

# Install dependencies
install:
	@echo "Installing dependencies..."
	poetry install

# Install development dependencies
dev:
	@echo "Installing development dependencies..."
	poetry install --with dev

# Run tests
test:
	@echo "Running tests..."
	poetry run pytest tests/ -v --cov=vox_tools --cov=apps --cov-report=html --cov-report=term

# Run linters
lint:
	@echo "Running linters..."
	poetry run ruff check vox_tools/ apps/ tests/ scripts/
	poetry run ruff check --fix vox_tools/ apps/ tests/ scripts/

# Format code
format:
	@echo "Formatting code..."
	poetry run black vox_tools/ apps/ tests/ scripts/
	poetry run isort vox_tools/ apps/ tests/ scripts/

# Run type checker
typecheck:
	@echo "Running type checker..."
	poetry run mypy vox_tools/ apps/

# Run all quality checks
quality: lint format typecheck test
	@echo "All quality checks passed!"

# Generate icons
icons:
	@echo "Generating icons..."
	poetry run python scripts/export_icons.py

# Build wheels and binaries
build: icons
	@echo "Building wheels..."
	poetry build
	@echo "Building binaries with PyInstaller..."
	poetry run pyinstaller --clean --noconfirm apps/cli/main.py --name voxtools-cli --onefile --distpath dist/binaries
	poetry run pyinstaller --clean --noconfirm apps/tui/main.py --name voxtools-tui --onefile --distpath dist/binaries
	poetry run pyinstaller --clean --noconfirm apps/gui/main.py --name voxtools-gui --onefile --windowed --distpath dist/binaries
	@echo "Build complete! Check dist/ directory"

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Run CLI application
run-cli:
	@echo "Running CLI application..."
	poetry run voxtools --help

# Run TUI application
run-tui:
	@echo "Running TUI application..."
	poetry run voxtools tui

# Run GUI application
run-gui:
	@echo "Running GUI application..."
	poetry run voxtools gui

# Development server
dev-server:
	@echo "Starting development server..."
	poetry run mkdocs serve

# Build documentation
docs:
	@echo "Building documentation..."
	poetry run mkdocs build

# Deploy documentation
deploy-docs:
	@echo "Deploying documentation..."
	poetry run mkdocs gh-deploy

# Release (create tag and push)
release:
	@echo "Creating release..."
	@read -p "Enter version (e.g., v1.0.0): " version; \
	git tag -a $$version -m "Release $$version"; \
	git push origin $$version

# Check for updates
update:
	@echo "Checking for updates..."
	poetry update
	poetry run pre-commit autoupdate
