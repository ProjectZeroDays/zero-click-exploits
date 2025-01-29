
import subprocess

def active_defense(malicious_domain):
    print(f"Blocking malicious domain: {malicious_domain}")
    try:
        command = f"iptables -A OUTPUT -d {malicious_domain} -j REJECT"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"Failed to block domain: {e}")
