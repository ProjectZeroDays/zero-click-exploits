@echo off

REM Function to install dependencies
:install_dependencies
echo Installing dependencies...
call npm install
goto :eof

REM Function to build the Windows app
:build_app
echo Building Windows app...
call npm run build
goto :eof

REM Function to sign the app
:sign_app
echo Signing Windows app...
call signtool sign /f mycert.pfx /p mypassword /tr http://timestamp.digicert.com /td sha256 /fd sha256 /a build\MyApp.exe
goto :eof

REM Function to install the app on a connected device
:install_app
echo Installing Windows app on device...
call adb install build\MyApp.exe
goto :eof

REM Main function to execute all steps
:main
call :install_dependencies
call :build_app
call :sign_app
call :install_app
goto :eof

REM Execute the main function
call :main
