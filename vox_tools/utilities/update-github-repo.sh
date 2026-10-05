#!/bin/bash
# Script to update GitHub repository description and topics
# Repository: https://github.com/Olyren/Website

set -e

REPO="Olyren/Website"
DESCRIPTION="Professional business formation services platform for USA, Canada, UK, and Mexico. Form your business in 24 hours with complete documentation and expert support."
TOPICS="business-formation,llc-formation,corporation,company-formation,business-registration,usa-business,canada-business,uk-business,mexico-business,nextjs,typescript,prisma,supabase,stripe,resend,nextauth,business-services,legal-services,startup,entrepreneurship"

echo "📝 Updating GitHub repository: $REPO"
echo ""

# Check if GitHub CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) is not installed."
    echo ""
    echo "Install it from: https://cli.github.com/"
    echo "Or update manually at: https://github.com/$REPO/settings"
    echo ""
    echo "Description:"
    echo "$DESCRIPTION"
    echo ""
    echo "Topics:"
    echo "$TOPICS"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo "❌ Not authenticated with GitHub CLI."
    echo "Run: gh auth login"
    exit 1
fi

echo "✅ GitHub CLI found and authenticated"
echo ""

# Update description
echo "📝 Updating repository description..."
gh repo edit "$REPO" --description "$DESCRIPTION"

# Update topics
echo "🏷️  Updating repository topics..."
gh repo edit "$REPO" --add-topic business-formation
gh repo edit "$REPO" --add-topic llc-formation
gh repo edit "$REPO" --add-topic corporation
gh repo edit "$REPO" --add-topic company-formation
gh repo edit "$REPO" --add-topic business-registration
gh repo edit "$REPO" --add-topic usa-business
gh repo edit "$REPO" --add-topic canada-business
gh repo edit "$REPO" --add-topic uk-business
gh repo edit "$REPO" --add-topic mexico-business
gh repo edit "$REPO" --add-topic nextjs
gh repo edit "$REPO" --add-topic typescript
gh repo edit "$REPO" --add-topic prisma
gh repo edit "$REPO" --add-topic supabase
gh repo edit "$REPO" --add-topic stripe
gh repo edit "$REPO" --add-topic resend
gh repo edit "$REPO" --add-topic nextauth
gh repo edit "$REPO" --add-topic business-services
gh repo edit "$REPO" --add-topic legal-services
gh repo edit "$REPO" --add-topic startup
gh repo edit "$REPO" --add-topic entrepreneurship

echo ""
echo "✅ Repository updated successfully!"
echo ""
echo "📋 Updated details:"
echo "   Description: $DESCRIPTION"
echo "   Topics: $TOPICS"
echo ""
echo "🔗 View at: https://github.com/$REPO"
