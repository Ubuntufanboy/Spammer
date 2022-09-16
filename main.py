from os import system
print("Pick your operating system!")
print("[1] Windows")
print("[2] Linux")
answer = input(">>> ")

if answer == "1":
    system("cd installers")
    system("python spam3.0.py")
elif answer == "2":
    system("cd installers")
    system("bash ./install.sh")