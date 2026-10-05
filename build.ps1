# VoxTools PowerShell Build Script
# Cross-platform build and development commands

param(
    [Parameter(Position=0)]
    [string]$Command = "help",
    [string]$Version = "",
    [switch]$Clean = $false,
    [switch]$Verbose = $false
)

# Colors for output
$Colors = @{
    Red = "Red"
    Green = "Green"
    Yellow = "Yellow"
    Blue = "Blue"
    Cyan = "Cyan"
    White = "White"
}

function Write-ColorOutput {
    param([string]$Message, [string]$Color = "White")
    Write-Host $Message -ForegroundColor $Colors[$Color]
}

function Show-Help {
    Write-ColorOutput "VoxTools PowerShell Build Script" "Cyan"
    Write-ColorOutput "=====================================" "Cyan"
    Write-ColorOutput ""
    Write-ColorOutput "Available commands:" "Yellow"
    Write-ColorOutput ""
    Write-ColorOutput "Setup & Development:" "Blue"
    Write-ColorOutput "  setup          - Set up development environment" "White"
    Write-ColorOutput "  install        - Install dependencies" "White"
    Write-ColorOutput "  dev            - Install development dependencies" "White"
    Write-ColorOutput ""
    Write-ColorOutput "Code Quality:" "Blue"
    Write-ColorOutput "  test           - Run tests" "White"
    Write-ColorOutput "  lint           - Run linters (Ruff)" "White"
    Write-ColorOutput "  format         - Format code (Black, isort)" "White"
    Write-ColorOutput "  typecheck      - Run type checker (mypy)" "White"
    Write-ColorOutput "  quality        - Run all quality checks" "White"
    Write-ColorOutput ""
    Write-ColorOutput "Building:" "Blue"
    Write-ColorOutput "  build          - Build wheels and binaries" "White"
    Write-ColorOutput "  icons          - Generate icon files" "White"
    Write-ColorOutput "  clean          - Clean build artifacts" "White"
    Write-ColorOutput ""
    Write-ColorOutput "Running:" "Blue"
    Write-ColorOutput "  run-cli        - Run CLI application" "White"
    Write-ColorOutput "  run-tui        - Run TUI application" "White"
    Write-ColorOutput "  run-gui        - Run GUI application" "White"
    Write-ColorOutput ""
    Write-ColorOutput "Documentation:" "Blue"
    Write-ColorOutput "  docs           - Build documentation" "White"
    Write-ColorOutput "  serve          - Serve documentation locally" "White"
    Write-ColorOutput ""
    Write-ColorOutput "Examples:" "Yellow"
    Write-ColorOutput "  .\build.ps1 setup" "White"
    Write-ColorOutput "  .\build.ps1 build" "White"
    Write-ColorOutput "  .\build.ps1 run-gui" "White"
    Write-ColorOutput "  .\build.ps1 clean" "White"
}

function Invoke-Setup {
    Write-ColorOutput "Setting up development environment..." "Blue"
    
    # Check if Poetry is installed
    try {
        $poetryVersion = poetry --version
        Write-ColorOutput "Poetry found: $poetryVersion" "Green"
    } catch {
        Write-ColorOutput "Poetry not found. Please install Poetry first:" "Red"
        Write-ColorOutput "https://python-poetry.org/docs/#installation" "Yellow"
        exit 1
    }
    
    # Install dependencies
    Write-ColorOutput "Installing dependencies..." "Blue"
    poetry install
    
    # Install development dependencies
    Write-ColorOutput "Installing development dependencies..." "Blue"
    poetry install --with dev
    
    # Set up pre-commit hooks
    Write-ColorOutput "Setting up pre-commit hooks..." "Blue"
    poetry run pre-commit install
    
    Write-ColorOutput "Development environment ready!" "Green"
}

function Invoke-Install {
    Write-ColorOutput "Installing dependencies..." "Blue"
    poetry install
    Write-ColorOutput "Dependencies installed!" "Green"
}

function Invoke-Dev {
    Write-ColorOutput "Installing development dependencies..." "Blue"
    poetry install --with dev
    Write-ColorOutput "Development dependencies installed!" "Green"
}

function Invoke-Test {
    Write-ColorOutput "Running tests..." "Blue"
    if ($Verbose) {
        poetry run pytest tests/ -v --cov=vox_tools --cov=apps --cov-report=html --cov-report=term
    } else {
        poetry run pytest tests/ --cov=vox_tools --cov=apps --cov-report=term
    }
    Write-ColorOutput "Tests completed!" "Green"
}

function Invoke-Lint {
    Write-ColorOutput "Running linters..." "Blue"
    poetry run ruff check vox_tools/ apps/ tests/ scripts/
    if ($LASTEXITCODE -eq 0) {
        Write-ColorOutput "Linting passed!" "Green"
    } else {
        Write-ColorOutput "Linting failed!" "Red"
        exit 1
    }
}

function Invoke-Format {
    Write-ColorOutput "Formatting code..." "Blue"
    poetry run black vox_tools/ apps/ tests/ scripts/
    poetry run isort vox_tools/ apps/ tests/ scripts/
    Write-ColorOutput "Code formatted!" "Green"
}

function Invoke-TypeCheck {
    Write-ColorOutput "Running type checker..." "Blue"
    poetry run mypy vox_tools/ apps/
    if ($LASTEXITCODE -eq 0) {
        Write-ColorOutput "Type checking passed!" "Green"
    } else {
        Write-ColorOutput "Type checking failed!" "Red"
        exit 1
    }
}

function Invoke-Quality {
    Write-ColorOutput "Running all quality checks..." "Blue"
    Invoke-Lint
    Invoke-Format
    Invoke-TypeCheck
    Invoke-Test
    Write-ColorOutput "All quality checks passed!" "Green"
}

function Invoke-Build {
    Write-ColorOutput "Building VoxTools..." "Blue"
    
    # Generate icons first
    Write-ColorOutput "Generating icons..." "Blue"
    poetry run python scripts/export_icons.py
    
    # Build wheels
    Write-ColorOutput "Building wheels..." "Blue"
    poetry build
    
    # Build binaries with PyInstaller
    Write-ColorOutput "Building binaries..." "Blue"
    
    # CLI binary
    Write-ColorOutput "Building CLI binary..." "Blue"
    poetry run pyinstaller --clean --noconfirm apps/cli/main.py --name voxtools-cli --onefile --distpath dist/binaries
    
    # TUI binary
    Write-ColorOutput "Building TUI binary..." "Blue"
    poetry run pyinstaller --clean --noconfirm apps/tui/main.py --name voxtools-tui --onefile --distpath dist/binaries
    
    # GUI binary
    Write-ColorOutput "Building GUI binary..." "Blue"
    poetry run pyinstaller --clean --noconfirm apps/gui/main.py --name voxtools-gui --onefile --windowed --distpath dist/binaries
    
    Write-ColorOutput "Build complete! Check dist/ directory" "Green"
}

function Invoke-Icons {
    Write-ColorOutput "Generating icons..." "Blue"
    poetry run python scripts/export_icons.py
    Write-ColorOutput "Icons generated!" "Green"
}

function Invoke-Clean {
    Write-ColorOutput "Cleaning build artifacts..." "Blue"
    
    $directories = @("build", "dist", "*.egg-info", ".coverage", "htmlcov", ".pytest_cache", ".mypy_cache", ".ruff_cache")
    
    foreach ($dir in $directories) {
        if (Test-Path $dir) {
            Remove-Item -Recurse -Force $dir
            Write-ColorOutput "Removed $dir" "Yellow"
        }
    }
    
    # Remove __pycache__ directories
    Get-ChildItem -Path . -Recurse -Directory -Name "__pycache__" | ForEach-Object {
        Remove-Item -Recurse -Force $_
        Write-ColorOutput "Removed __pycache__ directory" "Yellow"
    }
    
    # Remove .pyc files
    Get-ChildItem -Path . -Recurse -Filter "*.pyc" | Remove-Item -Force
    Write-ColorOutput "Removed .pyc files" "Yellow"
    
    Write-ColorOutput "Clean complete!" "Green"
}

function Invoke-RunCli {
    Write-ColorOutput "Running CLI application..." "Blue"
    poetry run voxtools --help
}

function Invoke-RunTui {
    Write-ColorOutput "Running TUI application..." "Blue"
    poetry run voxtools tui
}

function Invoke-RunGui {
    Write-ColorOutput "Running GUI application..." "Blue"
    poetry run voxtools gui
}

function Invoke-Docs {
    Write-ColorOutput "Building documentation..." "Blue"
    poetry run mkdocs build
    Write-ColorOutput "Documentation built!" "Green"
}

function Invoke-Serve {
    Write-ColorOutput "Serving documentation locally..." "Blue"
    Write-ColorOutput "Open http://127.0.0.1:8000 in your browser" "Yellow"
    poetry run mkdocs serve
}

# Main script logic
switch ($Command.ToLower()) {
    "help" { Show-Help }
    "setup" { Invoke-Setup }
    "install" { Invoke-Install }
    "dev" { Invoke-Dev }
    "test" { Invoke-Test }
    "lint" { Invoke-Lint }
    "format" { Invoke-Format }
    "typecheck" { Invoke-TypeCheck }
    "quality" { Invoke-Quality }
    "build" { Invoke-Build }
    "icons" { Invoke-Icons }
    "clean" { Invoke-Clean }
    "run-cli" { Invoke-RunCli }
    "run-tui" { Invoke-RunTui }
    "run-gui" { Invoke-RunGui }
    "docs" { Invoke-Docs }
    "serve" { Invoke-Serve }
    default {
        Write-ColorOutput "Unknown command: $Command" "Red"
        Write-ColorOutput "Run '.\build.ps1 help' for available commands" "Yellow"
        exit 1
    }
}
