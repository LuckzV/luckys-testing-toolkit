#!/bin/bash
# Server Test Engineer Toolkit Installation Script
# Run this script to set up the toolkit on a Linux system

echo "Server Test Engineer Toolkit - Installation Script"
echo "=================================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    echo "Please install Python 3 and try again."
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "Found Python $python_version"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv toolkit_env

# Activate virtual environment
echo "Activating virtual environment..."
source toolkit_env/bin/activate

# Install requirements
echo "Installing required packages..."
pip install --upgrade pip
pip install -r requirements.txt

# Make main script executable
chmod +x server_test_toolkit.py

# Create desktop shortcut (optional)
if [ -d "$HOME/Desktop" ]; then
    echo "Creating desktop shortcut..."
    cat > "$HOME/Desktop/Server-Test-Toolkit.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Server Test Toolkit
Comment=Server Test Engineer Toolkit
Exec=$(pwd)/server_test_toolkit.py
Icon=applications-system
Terminal=true
Categories=System;Development;
EOF
    chmod +x "$HOME/Desktop/Server-Test-Toolkit.desktop"
fi

echo ""
echo "Installation complete!"
echo "====================="
echo "To run the toolkit:"
echo "  ./server_test_toolkit.py"
echo ""
echo "Or activate the virtual environment first:"
echo "  source toolkit_env/bin/activate"
echo "  python3 server_test_toolkit.py"
echo ""
echo "The toolkit is now ready to use!"
