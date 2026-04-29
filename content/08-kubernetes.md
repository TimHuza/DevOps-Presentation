# ☸️ Kubernetes

---

## 📌 What is Kubernetes?

Kubernetes is an **open-source container orchestration platform** used to manage and automate containerized applications.

It helps with:
- Deploying containers
- Scaling applications
- Managing container health

💡 Kubernetes is often called **K8s**

---

## ❓ Why Kubernetes is Needed

Managing a few containers with Docker is easy, but managing hundreds is difficult.

Kubernetes helps by:
- Automatically restarting failed containers
- Scaling applications up or down
- Distributing traffic between containers

💡 It automates container management in production environments.

---

## 🏗 Kubernetes Architecture

Kubernetes works using **Master Node** and **Worker Nodes**

### Master Node
Controls the cluster:
- API Server
- Scheduler
- Controller Manager

### Worker Node
Runs the application containers inside **Pods**

---

## 📦 Pods, Services, Deployments

### Pod
The smallest unit in Kubernetes.
- Runs one or more containers

### Service
Provides a stable way to access Pods.
- Balances traffic between Pods

### Deployment
Manages Pod replicas and updates.
- Keeps the desired number of Pods running

---

## 📈 Scaling Applications

One major feature of Kubernetes is **scaling**

It can:
- Increase Pods when traffic grows
- Reduce Pods when traffic decreases

Example:
```bash
kubectl scale deployment app --replicas=3
```

💡 This helps applications handle more users automatically.

---

## 🔄 Kubernetes vs Docker

| Feature | Docker | Kubernetes |
|--------|--------|------------|
| Main Role | Run containers | Manage containers |
| Scaling | Manual | Automatic |
| Load Balancing | Limited | Built-in |
| Use Case | Single container apps | Large distributed apps |

💡 Docker creates containers, Kubernetes manages them.

---

## ⚙️ Basic Kubernetes Workflow

1. Build container image using Docker
2. Deploy container to Kubernetes
3. Kubernetes creates Pods
4. Services expose the application
5. Deployments manage scaling and updates

This makes applications **reliable and scalable**

---

## 🚀 Summary

- Kubernetes manages containerized applications
- It automates deployment and scaling
- Pods run containers
- Services provide access
- Deployments manage updates