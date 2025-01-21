#!/bin/bash

# Install dependencies
install_dependencies() {
    echo "Installing dependencies..."
    pip install tkinter
}

# Run the GUI
run_gui() {
    echo "Running the GUI..."
    python3 src/gui.py
}

# Main function to execute all steps
main() {
    install_dependencies
    run_gui
}

# Execute the main function
main
