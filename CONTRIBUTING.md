# Contributing to VoxTools

Thanks for helping improve VoxTools!

## Code of Conduct
Please read and follow our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Development Setup
```bash
# Clone
git clone https://github.com/VoxHash/VoxTools.git
cd VoxTools

# Install deps
poetry install
poetry install --with dev

# Set up pre-commit hooks
poetry run pre-commit install

# Run tests
poetry run pytest
```

## Branching & Commit Style
- Branches: `feature/…`, `fix/…`, `docs/…`, `chore/…`
- Conventional Commits: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`

## Code Quality
Before committing, run:
```bash
poetry run ruff check --fix vox_tools/ apps/ tests/
poetry run black vox_tools/ apps/ tests/
poetry run isort vox_tools/ apps/ tests/
poetry run mypy vox_tools/ apps/
```

## Pull Requests
- Link related issues, add tests, update docs
- Follow the PR template
- Keep diffs focused
- Ensure all tests pass

## Creating Plugins
See [docs/creating-plugins.md](docs/creating-plugins.md) for detailed plugin development guide.

## Release Process
- Semantic Versioning
- Update [CHANGELOG.md](CHANGELOG.md)

For more details, see the full [Contributing Guide](https://voxhash.github.io/VoxTools/contributing/).
