import subprocess

def add_user():
	subprocess.run("net user pegasus /add")
add_user()

