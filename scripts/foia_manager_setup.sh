#!/bin/bash
#
# Installs Python 3 dependencies using pip.
#
# This script checks for Python 3, updates pip, and installs the required dependencies
# listed in requirements.txt. It handles potential authentication prompts.
#
# Requires Python 3 to be installed and in the system's PATH.

set -e

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed or not in your PATH. Please install Python 3."
    exit 1
fi

echo "Python 3 found."

# Check if pip is installed
if ! command -v pip3 &> /dev/null
then
    echo "pip3 is not installed. Please install pip for Python 3."
    exit 1
fi

echo "pip3 found."

# Update pip
echo "Updating pip..."
python3 -m pip install --upgrade pip
echo "pip updated successfully."

# Install dependencies from requirements.txt
echo "Installing dependencies from requirements.txt..."
python3 -m pip install -r requirements.txt
echo "Dependencies installed successfully."

echo "Script completed."