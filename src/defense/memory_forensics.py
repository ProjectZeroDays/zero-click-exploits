
import subprocess

def analyze_memory(memory_dump, profile):
    print("Analyzing memory for malware...")
    try:
        command = f"volatility -f {memory_dump} --profile={profile} malfind"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"Memory analysis failed: {e}")
