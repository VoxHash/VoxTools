#!/bin/bash
# Script to push all local updates to GitHub

set -e

echo "🔄 Checking repository status..."

cd /run/media/raider/Workstation/Business/Olyren/Website

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Not a git repository"
    exit 1
fi

# Check remote
REMOTE=$(git remote get-url origin 2>/dev/null || echo "")
if [ -z "$REMOTE" ]; then
    echo "❌ No remote repository configured"
    echo "Run: git remote add origin https://github.com/Olyren/Website.git"
    exit 1
fi

echo "📋 Remote: $REMOTE"
echo ""

# Check for uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    echo "📦 Staging all changes..."
    git add -A
    
    echo "💾 Committing changes..."
    git commit -m "Update repository configuration and cleanup

- Add .specstory to .gitignore
- Update LICENSE to proprietary (Olyren Consulting LLC with patent)
- Remove tracked files that should be ignored
- Clean up temporary documentation files
- Add GitHub authentication setup documentation
- Update .gitignore with comprehensive exclusions" || echo "No changes to commit"
else
    echo "✅ No uncommitted changes"
fi

# Check if we're ahead of remote
LOCAL=$(git rev-parse @ 2>/dev/null)
REMOTE_REF=$(git ls-remote origin main 2>/dev/null | cut -f1)

if [ -z "$REMOTE_REF" ]; then
    echo "⚠️  Cannot reach remote. Checking authentication..."
    echo ""
    echo "If authentication fails, run: ./setup-github-auth.sh"
    echo ""
fi

echo "🚀 Pushing to origin/main..."
if git push origin main 2>&1; then
    echo ""
    echo "✅ Successfully pushed to GitHub!"
    echo "🔗 Repository: https://github.com/Olyren/Website"
else
    echo ""
    echo "❌ Push failed. Possible issues:"
    echo "   1. Authentication required - run: ./setup-github-auth.sh"
    echo "   2. Network connectivity issue"
    echo "   3. Remote repository access denied"
    echo ""
    echo "To set up authentication:"
    echo "   ./setup-github-auth.sh"
    exit 1
fi

echo ""
echo "🔍 Verifying ignored files are not tracked..."
TRACKED=$(git ls-files | grep -E "\.(vscode|editorconfig|npmrc|nvmrc|specstory)$|^\.vscode/|^prisma/migrations/" || true)
if [ -z "$TRACKED" ]; then
    echo "✅ Confirmed: No ignored files are tracked"
else
    echo "⚠️  Warning: Some ignored files are still tracked:"
    echo "$TRACKED"
fi
