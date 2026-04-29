# 🔧 Git & GitHub

---

## 📌 What is Version Control?

Version Control is a system that helps track changes in files over time.

- Keeps history of changes
- Allows reverting to previous versions
- Enables collaboration between multiple developers

💡 Think of it like “track changes” but for code projects

---

## 🧰 What is Git?

Git is a **distributed version control system**.

- Tracks changes in code
- Works locally on your computer
- Fast and efficient
- Widely used in DevOps and software development

### Key Idea:
Every developer has a **full copy of the project history**

💡 Git is the core tool for managing code in DevOps

---

## 🌐 What is GitHub?

GitHub is a **cloud platform that hosts Git repositories**.

- Stores your code online
- Enables collaboration
- Provides tools like issues, pull requests, and actions

### Other similar platforms:
- GitLab
- Bitbucket

💡 GitHub = Git + collaboration + cloud

---

## ⚖️ Git vs GitHub

| Feature | Git | GitHub |
|--------|-----|--------|
| Type | Tool | Platform |
| Runs on | Local machine | Cloud |
| Purpose | Version control | Code hosting & collaboration |
| Internet needed | No | Yes |

💡 You can use Git without GitHub, but not GitHub without Git

---

## 💻 Basic Git Commands

These are the most important commands every beginner should know:

| Command | Description |
|--------|------------|
| `git init` | Initialize a repository |
| `git add` | Add files to staging |
| `git commit` | Save changes |
| `git push` | Upload to GitHub |
| `git pull` | Download changes |

---

### Example Workflow:

```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```

💡 This is the basic flow used in most projects

---

## 🌿 Branching and Merging

Branching allows you to work on different features without affecting the main code.

### Why use branches?

* Work safely on new features
* Fix bugs without breaking main code

### Common Branch:

* `main` (or `master`) → main version of the project

---

### Example:

```bash id="8f5k1p"
git branch feature-login
git checkout feature-login
```

---

### Merging:

Combines changes from one branch into another:

```bash id="p7s4lm"
git merge feature-login
```

💡 Branching is essential for teamwork and safe development

---

## 🤝 Collaboration using Pull Requests

A Pull Request (PR) is a way to **propose changes** to a repository.

### Workflow:

1. Create a branch
2. Make changes
3. Push to GitHub
4. Open a Pull Request
5. Review and merge

---

### Why Pull Requests?

* Code review by team members
* Discuss changes before merging
* Improve code quality

💡 PRs are a key part of professional DevOps workflows
