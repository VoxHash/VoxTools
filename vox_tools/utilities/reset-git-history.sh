#!/bin/bash
# Script to reset git history and force push as first commit
# WARNING: This will delete all commit history from the remote repository

set -e

echo "⚠️  WARNING: This will delete ALL commit history from the remote repository!"
echo "This action cannot be undone."
echo ""
read -p "Are you sure you want to continue? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "Aborted."
    exit 1
fi

# Get the remote URL
REMOTE_URL=$(git remote get-url origin 2>/dev/null || echo "")
if [ -z "$REMOTE_URL" ]; then
    echo "❌ No remote repository found. Please add a remote first:"
    echo "   git remote add origin <your-repo-url>"
    exit 1
fi

echo ""
echo "📋 Current remote: $REMOTE_URL"
echo "📋 Current branch: $(git branch --show-current)"
echo ""

# Create orphan branch (no history)
echo "🔄 Creating orphan branch..."
git checkout --orphan new-main

# Add all files
echo "📦 Staging all files..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Fresh start

- Removed all old commits"

# Delete old main branch
echo "🗑️  Deleting old main branch..."
git branch -D main 2>/dev/null || true

# Rename current branch to main
echo "🔄 Renaming branch to main..."
git branch -m main

# Force push to remote
echo ""
echo "🚀 Force pushing to remote (this will overwrite remote history)..."
read -p "Press Enter to continue with force push, or Ctrl+C to cancel..."

git push -f origin main

echo ""
echo "✅ Success! Repository history has been reset."
echo "📝 The remote repository now has only one commit (this one)."
echo ""
echo "⚠️  If others are working on this repo, they need to:"
echo "   git fetch origin"
echo "   git reset --hard origin/main"
