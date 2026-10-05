#!/bin/bash
# Script to push all local updates and ensure ignored files are not tracked

set -e

echo "🔄 Checking for tracked files that should be ignored..."

# Remove tracked files that should be ignored
FILES_TO_REMOVE=()

# Check and remove .vscode if tracked
if git ls-files | grep -q "^\.vscode/"; then
    echo "❌ Found .vscode/ tracked - removing..."
    git rm -r --cached .vscode 2>/dev/null || true
    FILES_TO_REMOVE+=(".vscode/")
fi

# Check and remove prisma/migrations if tracked
if git ls-files | grep -q "^prisma/migrations/"; then
    echo "❌ Found prisma/migrations/ tracked - removing..."
    git rm -r --cached prisma/migrations 2>/dev/null || true
    FILES_TO_REMOVE+=("prisma/migrations/")
fi

# Check individual config files
for file in .editorconfig .npmrc .nvmrc .specstory; do
    if git ls-files | grep -q "^$file$"; then
        echo "❌ Found $file tracked - removing..."
        git rm --cached "$file" 2>/dev/null || true
        FILES_TO_REMOVE+=("$file")
    fi
done

if [ ${#FILES_TO_REMOVE[@]} -eq 0 ]; then
    echo "✅ No ignored files are currently tracked"
else
    echo "✅ Removed ${#FILES_TO_REMOVE[@]} tracked file(s) that should be ignored"
fi

echo ""
echo "📦 Staging all changes..."
git add -A

echo ""
echo "📋 Current status:"
git status --short | head -20

echo ""
echo "💾 Committing changes..."
git commit -m "Update repository configuration

- Add .specstory to .gitignore
- Update LICENSE to proprietary (Olyren Consulting LLC with patent)
- Remove tracked files that should be ignored (.vscode, .editorconfig, .npmrc, .nvmrc, prisma/migrations)
- Clean up repository structure" || echo "No changes to commit"

echo ""
echo "🚀 Pushing to remote..."
git push origin main

echo ""
echo "✅ Push completed successfully!"
echo ""
echo "🔍 Verifying ignored files are not tracked..."
if git ls-files | grep -E "\.(vscode|editorconfig|npmrc|nvmrc|specstory)$|^\.vscode/|^prisma/migrations/"; then
    echo "⚠️  Warning: Some ignored files are still tracked"
else
    echo "✅ Confirmed: No ignored files are tracked"
fi
