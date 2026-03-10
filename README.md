# CLI Password Manager

**CLI_PASSWORD_MANAGER**
Created by **Yousef Rouatbi**

A **terminal-based password manager** designed for **simplicity, security, and a hacker-style terminal experience**. Store, retrieve, and manage passwords entirely from the command line with strong encryption and professional terminal aesthetics.

---

## 🔐 Features

* Securely store and retrieve passwords with **encryption**
* Generate **strong, random passwords** automatically
* Add, get, list, or delete accounts directly from the CLI
* Works entirely in **terminal / CLI** (no GUI required)
* Minimal dependencies for easy installation

---

## ⚙️ Requirements

* Python **3.9+**
* `pip` package manager

Python packages used:

* `cryptography` – for encryption
* `colorama` – for terminal colors

---

## 🚀 Installation

1. **Clone the repository**

```bash
git clone https://github.com/youssefrouatbi/CLI-Password-Manager.git
```

2. **Go into the project folder**

```bash
cd CLI-Password-Manager
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 💻 Usage

Run commands using Python in the terminal.

### Add a new account

```bash
python passman.py add <account_name>
```

* Enter your **master password**
* Enter a password for the account (or leave empty to generate a strong random password)

### Get a password

```bash
python passman.py get <account_name>
```

* Prints the stored password for the account

### List all accounts

```bash
python passman.py list
```

### Delete an account

```bash
python passman.py delete <account_name>
```

### Generate a random password

```bash
python passman.py gen
```

---

## 🎨 Example Terminal Output

```
   ____ _     ___ ___    _  _   _  ____ ___ _   _  __  __
  |  _ \ |   |_ _/ _ \  | || | | |/ ___|_ _| \ | | \ \/ /
  | |_) | |    | | | | | | || |_| | |    | ||  \| |  \  /
  |  __/| |___ | | |_| | |__   _| | |___ | || |\  |  /  \
  |_|   |_____|___\___/     |_|   \____|___|_| \_| /_/\_\

Created by Yousef Rouatbi
Python CLI Password Manager
Secure & Easy to Use

Starting CLI Password Manager...

Master password:
```

---

## 🔒 Security Notes

* Your passwords are stored locally in an **encrypted file**
* Never share your **master password**
* The master password is required for **every command**

---

## 💡 Tips

* Use the **generated random passwords** for maximum security
* Keep your **master password memorable but strong**
* Backup your encrypted database file regularly
