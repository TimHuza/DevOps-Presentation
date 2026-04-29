# ⚙️ Ansible

---

## 📌 What is Ansible?

Ansible is an **automation tool** used to manage and configure servers.

- Open-source
- Simple and easy to use
- Works over SSH

💡 Used in DevOps to automate repetitive tasks

---

## 🧠 Configuration Management Concept

Configuration Management means:

👉 Keeping systems **consistent and correctly configured**

### Examples:
- Installing software
- Updating servers
- Managing settings

💡 Instead of doing tasks manually, Ansible automates them

---

## 🤖 Agent vs Agentless

### Agent-Based:
- Requires software installed on each server

### Agentless (Ansible):
- No software needed on target machines
- Uses SSH to connect

✅ Ansible is **agentless**, making it simple and lightweight

---

## 🏗️ Ansible Architecture

Ansible has a simple structure:

- **Control Node** → where Ansible runs
- **Managed Nodes** → servers being controlled

Control Node ---> Managed Nodes


💡 One control node can manage many servers

---

## 📜 Playbooks and YAML

Ansible uses **Playbooks** to define tasks.

- Written in **YAML** (easy to read)
- Describe what actions to perform

### Example:
```yaml
- name: Install nginx
  hosts: web
  tasks:
    - name: Install package
      apt:
        name: nginx
        state: present
```
[web]
192.168.1.10
```

- Groups servers together
- Used by playbooks