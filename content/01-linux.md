# 🐧 Linux

---

## 📌 What is Linux?

Linux is an **operating system (OS)**.  
An operating system is the main software that helps your computer work.

- It acts as a bridge between **hardware** and **applications**
- Used in servers, cloud platforms, and DevOps environments
- Known for being **stable, secure, and customizable**

It connects:

- 🖥️ **Hardware** → keyboard, screen, CPU, memory, hard drive  
- 📱 **Software** → apps, games, browsers, tools

## 🤔 So What Makes Linux Special?

Linux is:

- **Open-source**
- **Free to use**
- **Stable**
- **Secure**
- **Fast**
- **Customizable**

🏢 Big Companies That Use Linux

- Google
- Amazon
- Netflix
- Meta (Facebook, Instagram)
- Tesla
- Uber
- Spotify

💡 Many developers and IT professionals prefer Linux because of its power and flexibility.

---

## 📁 Files in Linux

In Linux, **everything is treated as a file**:
- Text files
- Directories (folders)
- Devices (like disks)

### 📂 Directory Structure

Linux uses a **hierarchical file system**:
```
/
├── home/  ← User directories
├── etc/   ← Configuration files
├── var/   ← Variable data (logs, etc.)
└── bin/   ← Essential commands
```

### Important Directories:
- `/home` → User files
- `/etc` → Configuration files
- `/var` → Logs and variable data
- `/bin` → Essential commands

## 📁 Important Linux Directories

### 🏠 `/home` → Personal User Files

This is where normal users keep their personal data.

Examples:

```text
/home/tim
/home/alex
/home/sarah
```

Inside it you may find:

* Documents
* Downloads
* Pictures
* Desktop files

💡 Similar to `C:\Users\Tim` on Windows.

---

### ⚙️ `/etc` → System Settings / Configuration

This folder stores important system configuration files.

Examples:

* Network settings
* User account settings
* Installed service configs
* Password policies

💡 Think of it like the **settings menu** of Linux.

Example files:

```text
/etc/passwd
/etc/hosts
/etc/ssh/
```

---

### 📜 `/var` → Variable / Changing Data

Stores data that changes often.

Examples:

* Logs
* Cache
* Temporary databases
* Mail queues
* Website data

Common use:

```text
/var/log
```

Contains logs like:

* login history
* system errors
* service activity

💡 Admins use `/var/log` to troubleshoot problems.

---

### 🛠️ `/bin` → Basic Commands

Contains important commands needed by all users.

Examples:

```bash
ls
cp
mv
rm
cat
mkdir
```

These commands are usually stored in `/bin`.

💡 Without `/bin`, many terminal commands would not work.

---

### 🧪 `/tmp` → Temporary Files

Used for temporary data.

Examples:

* Installer files
* App temporary cache
* Session data

Files here are often deleted automatically after reboot.

💡 Like a scratchpad — used now, removed later.

---

### 📦 `/usr` → Installed Programs & Shared Files

Contains many installed applications and tools.

Examples:

```text
/usr/bin
/usr/lib
/usr/share
```

Used for:

* Applications
* Libraries
* Documentation
* Icons

💡 Many programs you install live here.

---

## 💻 Basic Commands in Linux

Linux is often controlled using the **command line (terminal)**.

### Common Commands:

| Command | Description |
|--------|------------|
| `ls` | List files |
| `cd` | Change directory |
| `pwd` | Show current directory |
| `mkdir` | Create folder |
| `rm` | Delete files |
| `cp` | Copy files |
| `mv` | Move/rename files |

### Example:
```bash
cd /home
ls
mkdir project
cd project
```

💡 DevOps engineers use these commands daily!

---

## 👤 Users and Groups in Linux

Linux is a **multi-user system**, meaning multiple users can use it safely.

### Users:

* Each user has a **username and home directory**
* Example: `/home/tim`

### Groups:

* Users can belong to groups
* Used to manage permissions efficiently

### Why it matters:

* Controls access to files and systems
* Important for security in DevOps

---

## 🔐 File Permissions and `chmod`

Every file in Linux has permissions:

```
-rwxr-xr--
```

### Breakdown:

* `r` → read
* `w` → write
* `x` → execute

### Permission Groups:

* Owner
* Group
* Others

---

### 🔧 Changing Permissions with `chmod`

Example:

```bash
chmod 755 file.sh
```

Meaning:

* Owner → full access
* Group → read & execute
* Others → read & execute

---

### 💡 Why Permissions Matter

* Protect sensitive data
* Control who can run scripts
* Essential for secure DevOps pipelines

---

## 🚀 Summary

* Linux is the **foundation of DevOps**
* Everything is treated as a **file**
* Command line is the main way to interact
* Users and permissions ensure **security**
* Used in servers, containers, and cloud systems

---

## 🎯 Key Takeaway

👉 If you understand Linux, you understand the **core environment where DevOps happens**

```

---

If you want, I can next:
- :contentReference[oaicite:0]{index=0}
- Or :contentReference[oaicite:1]{index=1}
```
