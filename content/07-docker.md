# 🐳 Docker

---

## 📌 What is Docker?

Docker is a platform that allows you to **build, run, and ship applications in containers**.

- Packages app + dependencies together
- Runs the same everywhere (dev, test, production)
- Lightweight and fast

💡 "It works on my machine" problem → solved with Docker

---

## ⚖️ Containers vs Virtual Machines

### Containers:
- Share the host OS
- Lightweight and fast
- Start in seconds

### Virtual Machines:
- Have their own OS
- Heavier and slower
- Take more resources

💡 Containers are more efficient for DevOps workflows

---

## 🧱 Docker Architecture

Main components:

- **Docker Client** → where you run commands
- **Docker Daemon** → runs containers
- **Docker Registry** → stores images (e.g., Docker Hub)
- **Docker Repository** → collection of image versions/tags
- **Docker Host** → machine where Docker runs

Flow:

Client → Daemon → Container

## 📦 Docker Images and Containers

### Image:
- Blueprint/template of an application
- Read-only

### Container:
- Running instance of an image

💡 Image = class, Container = object

---

## 📝 Dockerfile Basics

A Dockerfile is a script to **build Docker images**.

### Example:
```dockerfile
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

💡 Automates app setup

---

## 💻 Basic Docker Commands

| Command             | Description                 |
| ------------------- | --------------------------- |
| `docker build`           | Build image                 |
| `docker run`             | Run container               |
| `docker ps`              | List containers             |
| `docker pull`            | Download image              |
| `docker create`          | Create container only       |
| `docker start`           | Start existing container    |
| `docker stop`            | Stop running container      |
| `docker images`          | List images                 |
| `docker rm`              | Remove container            |
| `docker rmi`             | Remove image                |
| `docker container prune` | Remove stopped containers   |

### Example:

```bash
docker build -t myapp .
docker run -p 5000:5000 myapp
```