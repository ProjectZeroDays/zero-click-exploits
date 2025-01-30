#!/bin/bash

# Function to install dependencies
install_dependencies() {
    echo "Installing dependencies..."
    brew install python3
    pip3 install -r requirements.txt
}

# Function to run the application
run_application() {
    echo "Running the application..."
    python3 src/app.py
}

# Main function to execute all steps
main() {
    install_dependencies
    run_application
}

# Execute the main function
main
