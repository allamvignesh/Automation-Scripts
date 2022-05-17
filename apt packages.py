import os

print("[UPDATING...] Mirrors...")

os.system("clear && sudo apt update")
os.system("sudo apt list --upgradable > list.txt")

file = open("list.txt", 'r')
li = file.readlines()
os.system("rm list.txt")

for i in range(1, len(li)):
	pkg = li[i].split()[0]
	pkg = pkg[:pkg.find('/')]
	print(f"[({i}/{len(li)-2}) UPDATING] {pkg}\n")
	os.system(f"sudo apt install {pkg} -y")
	os.system("sudo apt autoremove -y")
	print(f"\n[({i}/{len(li)-2}) DONE] {pkg}")
