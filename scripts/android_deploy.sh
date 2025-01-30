#!/bin/bash

# Function to install dependencies
install_dependencies() {
    echo "Installing dependencies..."
    ./gradlew build
}

# Function to build the APK
build_apk() {
    echo "Building APK..."
    ./gradlew assembleRelease
}

# Function to sign the APK
sign_apk() {
    echo "Signing APK..."
    jarsigner -verbose -keystore mykeystore.keystore app/build/outputs/apk/release/app-release-unsigned.apk alias_name
}

# Function to align the APK
align_apk() {
    echo "Aligning APK..."
    zipalign -v 4 app/build/outputs/apk/release/app-release-unsigned.apk app/build/outputs/apk/release/app-release.apk
}

# Function to install the APK on a connected device
install_apk() {
    echo "Installing APK on device..."
    adb install app/build/outputs/apk/release/app-release.apk
}

# Main function to execute all steps
main() {
    install_dependencies
    build_apk
    sign_apk
    align_apk
    install_apk
}

# Execute the main function
main
