#!/bin/bash

# Function to install dependencies
install_dependencies() {
    echo "Installing dependencies..."
    pod install
}

# Function to build the iOS app
build_app() {
    echo "Building iOS app..."
    xcodebuild -workspace MyApp.xcworkspace -scheme MyApp -configuration Release
}

# Function to sign the app
sign_app() {
    echo "Signing iOS app..."
    xcodebuild -exportArchive -archivePath build/MyApp.xcarchive -exportPath build/MyApp -exportOptionsPlist exportOptions.plist
}

# Function to install the app on a connected device
install_app() {
    echo "Installing iOS app on device..."
    ideviceinstaller -i build/MyApp/MyApp.ipa
}

# Main function to execute all steps
main() {
    install_dependencies
    build_app
    sign_app
    install_app
}

# Execute the main function
main
