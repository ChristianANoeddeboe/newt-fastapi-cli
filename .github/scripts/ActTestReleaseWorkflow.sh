#!/bin/bash

# Local test script for GitHub Action workflow
# This tests the main logic without GitHub-specific actions

set -e  # Exit on any error

echo "🧪 Testing GitHub Action workflow locally..."
echo "================================================"

# Simulate inputs (you can change these)
VERSION_BUMP=${1:-"patch"}  # patch, minor, or major
RELEASE_NOTES=${2:-"Test release notes"}

echo "📝 Inputs:"
echo "  Version bump: $VERSION_BUMP"
echo "  Release notes: $RELEASE_NOTES"
echo ""

# 1. Test Python and Poetry setup
echo "🐍 Testing Python and Poetry setup..."
python3 --version
poetry --version
echo "✅ Python and Poetry are available"
echo ""

# 2. Install dependencies
echo "📦 Installing dependencies..."
poetry install
echo "✅ Dependencies installed"
echo ""

# 3. Run tests (if any)
echo "🧪 Running tests..."
if [ -d "tests" ] && [ "$(ls -A tests)" ]; then
    if poetry run python -c "import pytest" 2>/dev/null; then
        poetry run pytest --verbose
    else
        echo "pytest not installed, skipping tests"
    fi
else
    echo "No tests found, skipping test step"
fi
echo "✅ Tests completed"
echo ""

# 4. Test CLI functionality
echo "🔧 Testing CLI functionality..."
poetry run newt --help > /dev/null
poetry run newt -v
echo "✅ CLI is working"
echo ""

# 5. Get current version
CURRENT_VERSION=$(poetry version -s)
echo "📋 Current version: $CURRENT_VERSION"

# 6. Simulate version bump (without committing)
echo "🔄 Simulating version bump ($VERSION_BUMP)..."
poetry version $VERSION_BUMP
NEW_VERSION=$(poetry version -s)
echo "📋 New version would be: $NEW_VERSION"

# 7. Test build
echo "🏗️  Testing build..."
poetry build
echo "✅ Build completed successfully"

# 8. Check built files
echo "📄 Built files:"
ls -la dist/

echo ""
echo "🎉 Local test completed successfully!"
echo "   Current version: $CURRENT_VERSION"
echo "   New version: $NEW_VERSION"
echo "   Built files are in ./dist/"
echo ""
echo "💡 To test with different version bump:"
echo "   ./test_workflow.sh minor"
echo "   ./test_workflow.sh major"

# Reset version back to original (since this is just a test)
echo "🔄 Resetting version back to original..."
poetry version $CURRENT_VERSION > /dev/null
echo "✅ Version reset to $CURRENT_VERSION"