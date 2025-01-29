import shutil, os, subprocess


def hide_file():

	path = 'attrib +s +h "C:\\Users\\Dell\\OneDrive\\Desktop\\pegasus\\1. hide_your_pegasus\\hide_pegasus.py"'
	subprocess.call(path, shell= True)
	

hide_file()




