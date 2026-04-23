# 🐧 Linux

---

## 📌 What is Linux?

Linux is an **open-source operating system** that manages hardware and software resources on a computer.

- It acts as a bridge between **hardware** and **applications**
- Used in servers, cloud platforms, and DevOps environments
- Known for being **stable, secure, and customizable**

💡 Most servers on the internet run Linux!

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
