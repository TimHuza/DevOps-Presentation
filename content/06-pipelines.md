# 🔗 Pipelines

## 📌 What is a Pipeline?

A pipeline is a **series of automated steps** to deliver software.

👉 It defines how code moves from development → production

---

## 🧠 Pipeline as Code

* Pipelines are written in code (e.g., Jenkinsfile)
* Stored in Git
* Easy to version and reuse

💡 Everything in DevOps is automated using code

### 📄 What is a Jenkinsfile?

A **Jenkinsfile** is a file that defines the pipeline steps Jenkins should run.

It contains instructions like:
- how to build the application,
- what tests to run,
- and how to deploy the software.

### 🧠 Simple Explanation

Think of a Jenkinsfile like a recipe for Jenkins.

Example:
- Step 1 → Build app
- Step 2 → Run tests
- Step 3 → Deploy app

Jenkins reads the Jenkinsfile and follows the instructions automatically.

### ✅ Why Jenkinsfile is Used

- Pipelines can be stored in Git with the application code
- Teams can track changes to pipelines
- Easier collaboration between developers
- Same pipeline can be reused many times
- Helps automate everything consistently

💡 This concept is called **Pipeline as Code**.

## 📄 Simple Jenkinsfile Example

```groovy
pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building the application...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }
}
```

---

## 🧩 Stages in a Pipeline

Typical stages:

1. Build
2. Test
3. Deploy

---

## 🔄 Example Pipeline Flow

```id="g7m2zx"
Build → Test → Deploy
```

* Build the app
* Test for errors
* Deploy to server

---

## ⚙️ Jenkins Pipelines

* **Declarative** → Simple and structured
* **Scripted** → More flexible

👉 Beginners usually start with Declarative

---

## 🌟 Advantages of Pipelines

* Full automation
* Consistent process
* Faster delivery
* Easy to track issues

---

## 🚀 Summary

* Pipelines automate the software lifecycle
* Used with tools like Jenkins
* Key part of modern DevOps