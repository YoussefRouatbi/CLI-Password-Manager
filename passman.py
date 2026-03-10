import json
import os
import base64
import secrets
from cryptography.fernet import Fernet
import hashlib
from colorama import Fore, Style, init
import time


init(autoreset=True)

banner = f"""
{Fore.CYAN}
   ____ _     ___ ___    _  _   _  ____ ___ _   _  __  __
  |  _ \ |   |_ _/ _ \  | || | | |/ ___|_ _| \ | | \ \/ /
  | |_) | |    | | | | | | || |_| | |    | ||  \| |  \  / 
  |  __/| |___ | | |_| | |__   _| | |___ | || |\  |  /  \ 
  |_|   |_____|___\___/     |_|   \____|___|_| \_| /_/\_\

{Fore.YELLOW}Created by Youssef Rouatbi
Python CLI Password Manager
Secure & Easy to Use
"""


for line in banner.splitlines():
    print(line)
    time.sleep(0.03)

print(Fore.GREEN + "\nStarting CLI Password Manager...\n")
time.sleep(0.2)

DATA_FILE = "vault.dat"

def generate_key(master_password):
    return base64.urlsafe_b64encode(hashlib.sha256(master_password.encode()).digest())

def load_vault(key):
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "rb") as f:
        encrypted = f.read()
    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(encrypted)
    except Exception:
        print(Fore.RED + "Error: Master password incorrect or vault corrupted!")
        exit(1)
    return json.loads(decrypted.decode())

def save_vault(vault, key):
    fernet = Fernet(key)
    data = json.dumps(vault).encode()
    encrypted = fernet.encrypt(data)
    with open(DATA_FILE, "wb") as f:
        f.write(encrypted)

def generate_password(length=16):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def add_password(vault, key):
    service = input("Enter service name: ")
    password = input("Password (leave empty to generate): ")
    if password == "":
        password = generate_password()
        print(Fore.GREEN + "Generated password:", password)
    vault[service] = password
    save_vault(vault, key)
    print(Fore.GREEN + f"Password for '{service}' saved successfully!")

def get_password(vault):
    service = input("Enter service name: ")
    if service in vault:
        print(Fore.CYAN + f"Password for '{service}': {vault[service]}")
    else:
        print(Fore.RED + f"Service '{service}' not found!")

def list_services(vault):
    if vault:
        print(Fore.YELLOW + "Saved services:")
        for service in vault:
            print(Fore.CYAN + f"- {service}")
    else:
        print(Fore.YELLOW + "No services stored yet.")

def delete_password(vault, key):
    service = input("Enter service name to delete: ")
    if service in vault:
        del vault[service]
        save_vault(vault, key)
        print(Fore.GREEN + f"Service '{service}' deleted successfully!")
    else:
        print(Fore.RED + f"Service '{service}' not found!")

def main():
    master = input(Fore.MAGENTA + "Master password: ")
    key = generate_key(master)
    vault = load_vault(key)

    while True:
        print(Fore.BLUE + "\n--- Menu ---")
        print("1) Add password")
        print("2) Get password")
        print("3) List services")
        print("4) Delete password")
        print("5) Generate random password")
        print("6) Exit")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            add_password(vault, key)
        elif choice == "2":
            get_password(vault)
        elif choice == "3":
            list_services(vault)
        elif choice == "4":
            delete_password(vault, key)
        elif choice == "5":
            print(Fore.GREEN + "Generated password:", generate_password())
        elif choice == "6":
            print(Fore.YELLOW + "Exiting... Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid option. Try again.")

if __name__ == "__main__":
    main()