#!/bin/bash
# Quick GitHub authentication setup script

set -e

echo "🔐 GitHub Authentication Setup"
echo ""
echo "This script will help you set up GitHub authentication using a Personal Access Token."
echo ""
echo "📋 Steps:"
echo "1. Go to: https://github.com/settings/tokens"
echo "2. Click 'Generate new token (classic)'"
echo "3. Name it: 'Olyren Website Repository Access'"
echo "4. Select scope: 'repo' (all checkboxes)"
echo "5. Generate and copy the token"
echo ""
read -p "Press Enter when you have your token ready..."

echo ""
echo "Enter your GitHub Personal Access Token:"
echo "(Token will be hidden for security)"
read -s GITHUB_TOKEN

if [ -z "$GITHUB_TOKEN" ]; then
    echo "❌ Token cannot be empty"
    exit 1
fi

echo ""
echo "Enter your GitHub username:"
read GITHUB_USERNAME

if [ -z "$GITHUB_USERNAME" ]; then
    echo "❌ Username cannot be empty"
    exit 1
fi

cd /run/media/raider/Workstation/Business/Olyren/Website

# Update remote URL with token
echo ""
echo "🔄 Updating remote URL..."
git remote set-url origin https://${GITHUB_TOKEN}@github.com/Olyren/Website.git

# Also set up credential helper for future use
echo "💾 Configuring credential helper..."
git config --global credential.helper store

# Store credentials (username:token)
echo "https://${GITHUB_USERNAME}:${GITHUB_TOKEN}@github.com" > ~/.git-credentials
chmod 600 ~/.git-credentials

echo ""
echo "🧪 Testing connection..."

if git ls-remote origin &>/dev/null; then
    echo "✅ Authentication successful!"
    echo ""
    echo "📋 Repository information:"
    git remote -v
    echo ""
    echo "🚀 You can now push your changes:"
    echo "   git push origin main"
    echo ""
    echo "✅ Credentials have been saved for future use."
else
    echo "❌ Authentication failed."
    echo ""
    echo "Please check:"
    echo "  - Token is correct (starts with ghp_)"
    echo "  - Token has 'repo' scope enabled"
    echo "  - Repository exists: https://github.com/Olyren/Website"
    echo "  - You have push access to the repository"
    exit 1
fi
