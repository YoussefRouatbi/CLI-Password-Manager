# CLI Password Manager

**CLI_PASSWORD_MANAGER**
Created by **Yousef Rouatbi**

A **terminal-based password manager** designed for **simplicity, security, and a hacker-style terminal experience**. Store, retrieve, and manage passwords entirely from the command line with strong encryption and professional terminal aesthetics.

---

## 🔐 Features

* Securely store and retrieve passwords with **Fernet encryption** using a master password
* Generate **strong, random passwords** automatically
* Add, get, list, or delete accounts directly from the CLI menu
* Works entirely in **terminal / CLI** (no GUI required)
* ASCII banner and **colored terminal output** for a hacker-style vibe
* Minimal dependencies: `cryptography` and `colorama`

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

Run the program in the terminal with Python:

```bash
python passman.py
```

You will see a **hacker-style ASCII banner** and be prompted for your **master password**. Once logged in, you can use the CLI menu to:

### Menu Options

1. **Add password** – Add a new service and its password (or generate one automatically)
2. **Get password** – Retrieve the password for a service
3. **List services** – View all saved services
4. **Delete password** – Remove a service and its password
5. **Generate random password** – Create a strong random password
6. **Exit** – Close the program

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

* Your passwords are stored locally in an **encrypted file `vault.dat`**
* Never share your **master password**
* The master password is required for **every session**
* Strong passwords are generated using the `secrets` module for maximum randomness

---

## 💡 Tips

* Use the **generated random passwords** for maximum security
* Keep your **master password memorable but strong**
* Backup your encrypted `vault.dat` file regularly
