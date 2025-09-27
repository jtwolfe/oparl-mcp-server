#!/bin/bash
# GitHub Pages Setup Script for OParl MCP Server

set -e

echo "🚀 Setting up GitHub Pages for OParl MCP Server"
echo "=============================================="

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Error: Not in a git repository"
    exit 1
fi

# Check if we're on GitHub
if ! git remote get-url origin | grep -q "github.com"; then
    echo "❌ Error: Not a GitHub repository"
    exit 1
fi

echo "✅ Git repository detected"

# Check if docs directory exists
if [ ! -d "docs" ]; then
    echo "❌ Error: docs directory not found"
    exit 1
fi

echo "✅ Documentation directory found"

# Check if Jekyll configuration exists
if [ ! -f "docs/_config.yml" ]; then
    echo "❌ Error: Jekyll configuration not found"
    exit 1
fi

echo "✅ Jekyll configuration found"

# Check if GitHub Actions workflow exists
if [ ! -f ".github/workflows/docs-jekyll.yml" ]; then
    echo "❌ Error: GitHub Actions workflow not found"
    exit 1
fi

echo "✅ GitHub Actions workflow found"

echo ""
echo "📋 Next Steps:"
echo "=============="
echo ""
echo "1. Push your changes to GitHub:"
echo "   git add ."
echo "   git commit -m 'Add Jekyll documentation setup'"
echo "   git push origin main"
echo ""
echo "2. Enable GitHub Pages:"
echo "   - Go to your repository on GitHub"
echo "   - Navigate to Settings → Pages"
echo "   - Under 'Source', select 'GitHub Actions'"
echo "   - The documentation will be built automatically"
echo ""
echo "3. Access your documentation:"
echo "   https://jtwolfe.github.io/oparl-mcp-server"
echo ""
echo "4. Monitor the build:"
echo "   - Go to the Actions tab in your repository"
echo "   - Check the 'Build and Deploy Jekyll Documentation' workflow"
echo ""

# Check if we can determine the repository URL
REPO_URL=$(git remote get-url origin)
if [[ $REPO_URL == *"github.com"* ]]; then
    # Extract owner and repo name
    if [[ $REPO_URL == *"git@github.com:"* ]]; then
        REPO_PATH=${REPO_URL#git@github.com:}
    elif [[ $REPO_URL == *"https://github.com/"* ]]; then
        REPO_PATH=${REPO_URL#https://github.com/}
    fi

    REPO_PATH=${REPO_PATH%.git}

    echo "🔗 Repository Information:"
    echo "   Repository: $REPO_PATH"
    echo "   Documentation URL: https://${REPO_PATH%/*}.github.io/${REPO_PATH##*/}"
    echo ""
fi

echo "✅ Setup script completed successfully!"
echo ""
echo "📚 For more information, see GITHUB_PAGES_SETUP.md"
