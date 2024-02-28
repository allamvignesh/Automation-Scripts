import subprocess
import sys

subprocess.call("pip install --upgrade pip --user")

packages = [i[:i.find('=')] for i in subprocess.getoutput("pip list --outdated").split('\n')]
a = input("[GUIDE] Do you want to upgrade all packages: ")

for i in range(1, len(packages)):
    print(f"\n[ ({i+1}/{len(packages)})PACKAGE] {packages[i]}")
    if a.lower() == 'yes' or a.lower() == 'y':
        subprocess.call(f"pip install -U {packages[i]}")
    else:
        inp = input(f"[GUIDE] Do you want to install {packages[i]}: ")
        if inp.lower() == "yes" or inp.lower() == 'y':
            subprocess.call(f"pip install -U {packages[i]}")
