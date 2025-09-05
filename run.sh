#!/bin/bash
# Quick launcher for Server Test Engineer Toolkit

echo "Server Test Engineer Toolkit - Quick Launcher"
echo "============================================="

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    echo "Please install Python 3 and try again."
    exit 1
fi

# Check if virtual environment exists
if [ -d "toolkit_env" ]; then
    echo "Activating virtual environment..."
    source toolkit_env/bin/activate
else
    echo "Virtual environment not found. Running with system Python..."
    echo "For best results, run ./install.sh first"
fi

# Check if requirements are installed
python3 -c "import psutil" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Warning: Some dependencies may not be installed."
    echo "Run ./install.sh to install all requirements."
    echo ""
fi

# Run the toolkit
echo "Starting Server Test Engineer Toolkit..."
python3 server_test_toolkit.py "$@"
