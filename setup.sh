#!/bin/bash

echo "🐺 WOLFY SETUP SCRIPT 🐺"
echo ""
echo "Setting up your mesh concert environment..."
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv

# Activate and install dependencies
echo "Installing dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "To use Wolfy:"
echo "  1. Activate the virtual environment:"
echo "     source venv/bin/activate"
echo ""
echo "  2. Run the concert:"
echo "     python run_wolfy_concert.py"
echo ""
echo "  3. Or run a quick test:"
echo "     python quick_test.py"
echo ""
echo "🐺 Enjoy the concert! 🐺"

