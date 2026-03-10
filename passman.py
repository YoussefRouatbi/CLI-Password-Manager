import argparse
import json
import os
import base64
import secrets
from cryptography.fernet import Fernet
import hashlib
from colorama import Fore, Style, init
import time

# Initialize colorama
init(autoreset=True)

# ASCII Art banner
banner = f"""
{Fore.CYAN}
   ____ _     ___ ___    _  _   _  ____ ___ _   _  __  __
  |  _ \ |   |_ _/ _ \  | || | | |/ ___|_ _| \ | | \ \/ /
  | |_) | |    | | | | | | || |_| | |    | ||  \| |  \  / 
  |  __/| |___ | | |_| | |__   _| | |___ | || |\  |  /  \ 
  |_|   |_____|___\___/     |_|   \____|___|_| \_| /_/\_\

{Fore.YELLOW}Created by Yousef Rouatbi
Python CLI Password Manager
Secure & Easy to Use
"""

# Show banner like “hacker” style
for line in banner.splitlines():
    print(line)
    time.sleep(0.05)  # small delay for effect

print(Fore.GREEN + "\nStarting CLI Password Manager...\n")
time.sleep(0.3)

DATA_FILE = "vault.dat"
KEY_FILE = "key.key"


def generate_key(master_password):
    return base64.urlsafe_b64encode(hashlib.sha256(master_password.encode()).digest())


def load_vault(key):
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "rb") as f:
        encrypted = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted)

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


def main():
    parser = argparse.ArgumentParser(description="CLI Password Manager")
    parser.add_argument("command", choices=["add", "get", "list", "delete", "gen"])
    parser.add_argument("service", nargs="?")
    args = parser.parse_args()

    master = input("Master password: ")
    key = generate_key(master)

    vault = load_vault(key)

    if args.command == "add":
        password = input("Password (leave empty to generate): ")

        if password == "":
            password = generate_password()
            print("Generated password:", password)

        vault[args.service] = password
        save_vault(vault, key)

        print("Saved.")

    elif args.command == "get":
        if args.service in vault:
            print("Password:", vault[args.service])
        else:
            print("Service not found")

    elif args.command == "list":
        for service in vault:
            print(service)

    elif args.command == "delete":
        if args.service in vault:
            del vault[args.service]
            save_vault(vault, key)
            print("Deleted.")
        else:
            print("Service not found")

    elif args.command == "gen":
        print(generate_password())


if __name__ == "__main__":
    main()