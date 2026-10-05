# Script to track and commit all changes in the repository
# Usage: .\track-changes.ps1 [commit-message]

param(
    [string]$CommitMessage = "Update tracked files"
)

Write-Host "=== Tracking All Changes ===" -ForegroundColor Cyan

# Check for uncommitted changes
Write-Host ""
Write-Host "Checking for uncommitted changes..." -ForegroundColor Yellow
$status = git status --porcelain

if ($status) {
    Write-Host "Found uncommitted changes:" -ForegroundColor Green
    git status --short
    
    # Add all changes
    Write-Host ""
    Write-Host "Staging all changes..." -ForegroundColor Yellow
    git add -A
    
    # Show what will be committed
    Write-Host ""
    Write-Host "Changes to be committed:" -ForegroundColor Yellow
    git status --short
    
    # Commit changes
    Write-Host ""
    Write-Host "Committing changes..." -ForegroundColor Yellow
    git commit -m $CommitMessage
    
    Write-Host ""
    Write-Host "Changes committed successfully!" -ForegroundColor Green
} else {
    Write-Host "No uncommitted changes found." -ForegroundColor Green
}

# Check if local is ahead of remote
Write-Host ""
Write-Host "Checking sync status with remote..." -ForegroundColor Yellow
git fetch origin --quiet
$localCommits = git log origin/main..HEAD --oneline

if ($localCommits) {
    Write-Host "Local commits not yet pushed:" -ForegroundColor Yellow
    $localCommits | ForEach-Object { Write-Host "  $_" }
    
    Write-Host ""
    $push = Read-Host "Push to remote? (y/n)"
    if ($push -eq 'y' -or $push -eq 'Y') {
        Write-Host ""
        Write-Host "Pushing to remote..." -ForegroundColor Yellow
        git push origin main
        Write-Host "Pushed successfully!" -ForegroundColor Green
    }
} else {
    Write-Host "Local repository is in sync with remote." -ForegroundColor Green
}

Write-Host ""
Write-Host "=== Complete ===" -ForegroundColor Cyan
