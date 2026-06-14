## 📋 PROJECT OVERVIEW

Build a **full-stack web application** that serves as a professional, interactive **DevOps training presentation** authored by **Tim Huza**, complete with an attendee **sign-up system** that saves registrant data to a **MySQL database**.

---

## 🎯 APPLICATION GOALS

1. Display a sleek, dark-themed, multi-slide **DevOps presentation** covering 13 topic sections
2. Allow visitors to **register as attendees** by submitting their first name, last name, and email
3. Persist all registrant data in a **MySQL database table**
4. Provide a clean, modern UI that feels premium and professional

---

## 🗂️ PRESENTATION CONTENT STRUCTURE

The presentation has **13 sections** displayed as navigable slides. Reproduce all of the following topic sections in order:

### Slide 0 — Title / Hero Slide
- Title: **"DevOps — From Zero to Production"**
- Subtitle: *"Linux · Networking · Git · Jenkins · CI/CD · Pipelines · Docker · Kubernetes · Ansible · Terraform · IaC · Python"*
- Author badge: **Tim Huza**
- Display a row of topic chip badges for each major section
- Dark radial gradient background (indigo → near-black)
- Include a prominent **"Register as Attendee"** call-to-action button that opens the sign-up form

### Slide 1 — Linux 🐧
Cover these sub-topics (one slide or section each):
- What is Linux? (OS bridge between hardware and apps; open-source, stable, secure, fast)
- Big companies that use Linux: Google, Amazon, Netflix, Meta, Tesla, Uber, Spotify
- Files in Linux (everything is a file; hierarchical directory structure: `/`, `/home`, `/etc`, `/var`, `/bin`, `/tmp`, `/usr`)
- Basic Terminal Commands table: `ls`, `cd`, `pwd`, `mkdir`, `rm`, `cp`, `mv`
- Users and Groups (multi-user system; `/home/username`; group-based permissions)
- File Permissions and `chmod` (`rwxr-xr--` breakdown; `chmod 755 file.sh` example)
- Summary: Linux is the foundation of DevOps

### Slide 2 — Network Basics 🌐
- What is a Network? (devices communicating to share resources)
- IP Address (unique identifier; IPv4 vs IPv6 example)
- LAN — Local Area Network (home/office scope)
- WAN — Wide Area Network (internet scope; ISP connection)
- HTTP — HyperText Transfer Protocol (stateless; port 80; request/response cycle)
- HTTPS — Secure HTTP (TLS/SSL encryption; port 443; padlock icon)
- TCP — Transmission Control Protocol (connection-oriented; reliable; 3-way handshake)
- UDP — User Datagram Protocol (connectionless; fast; used in video/gaming)

### Slide 3 — Git & GitHub 🐙
- What is Version Control? (track changes; revert; collaborate)
- What is Git? (distributed VCS; local repo)
- What is GitHub? (cloud hosting for Git; collaboration platform)
- Git vs GitHub comparison table
- Basic Git Commands: `git init`, `git add .`, `git commit -m ""`, `git push`, `git pull`, `git clone`
- Branching and Merging (feature branches; `git branch`, `git merge`, `git checkout`)
- Pull Requests (code review; merge into main)

### Slide 4 — Jenkins 🔧
- What is Jenkins? (open-source automation server; CI/CD tool)
- Why Jenkins in DevOps? (automates builds, tests, deployments)
- Jenkins Architecture (Master node orchestrates; Agent/Worker nodes execute jobs)
- Installing Jenkins (Java dependency; war file or Docker; port 8080)
- Creating a Simple Job (Freestyle vs Pipeline job)
- Plugins in Jenkins (1,800+ plugins; Git, Docker, Slack, Maven integrations)
- Jenkins in Automation (triggered by code push; webhook integration)

### Slide 5 — CI/CD ♾️
- What is CI/CD? (methodology to automate code integration and delivery)
- Continuous Integration (CI): auto-build and test on every commit
- Continuous Delivery: code always deployable; manual production gate
- Continuous Deployment: fully automated push to production
- Benefits of CI/CD (faster releases; fewer bugs; consistent quality)
- CI/CD Workflow: Code → Commit → Build → Test → Stage → Deploy
- Tools: Jenkins, GitHub Actions, GitLab CI, CircleCI, ArgoCD

### Slide 6 — Pipelines 🔀
- What is a Pipeline? (series of automated steps to ship code)
- Pipeline as Code (stored in repo; version controlled; reproducible)
- Stages: Build → Test → Security Scan → Artifact → Deploy
- Example Jenkinsfile (declarative syntax with stages and steps)
- Declarative vs Scripted Pipeline comparison
- Advantages: visibility, repeatability, auditability

### Slide 7 — Docker 🐳
- What is Docker? (containerization platform; package app + dependencies)
- Containers vs Virtual Machines (Docker: shares OS kernel; VMs: full OS per instance; comparison table)
- Docker Architecture: Docker Engine, Daemon, CLI, Registry
- Docker Images vs Containers (image = blueprint; container = running instance)
- Dockerfile Basics: `FROM`, `COPY`, `RUN`, `EXPOSE`, `CMD`
- Basic Docker Commands: `docker build`, `docker run`, `docker ps`, `docker pull`, `docker stop`
- Why Docker in DevOps? ("works on my machine" problem solved; consistent environments)

### Slide 8 — Kubernetes ☸️
- What is Kubernetes (K8s)? (container orchestration platform by Google)
- Why Kubernetes is Needed (manage hundreds/thousands of containers)
- Architecture: Control Plane (API Server, etcd, Scheduler) + Worker Nodes (kubelet, kube-proxy, pods)
- Pods — smallest deployable unit (one or more containers)
- Services — expose pods with stable endpoints (ClusterIP, NodePort, LoadBalancer)
- Deployments — declarative management of pod replicas and rolling updates
- Scaling: `kubectl scale deployment app --replicas=5`
- Kubernetes vs Docker comparison
- Basic Workflow: write YAML manifests → `kubectl apply -f` → K8s handles the rest

### Slide 9 — Ansible ⚙️
- What is Ansible? (agentless IT automation tool by Red Hat)
- Configuration Management (ensure servers are in desired state)
- Agent vs Agentless (Ansible uses SSH; no software on managed nodes)
- Ansible Architecture: Control Node → Inventory → Modules → Playbooks
- Playbooks (YAML files defining tasks to run on hosts)
- Inventory File (list of hosts by group: `[webservers]`, `[databases]`)
- Common Use Cases: provisioning servers, deploying apps, managing configs, orchestrating workflows

### Slide 10 — Terraform 🌿
- What is Terraform? (Infrastructure as Code tool by HashiCorp)
- Infrastructure Provisioning (create cloud resources with code)
- Terraform vs Ansible comparison (Terraform = provision infra; Ansible = configure it)
- Providers (AWS, GCP, Azure, Kubernetes, GitHub plugins)
- Writing a Basic `.tf` Configuration (provider block + resource block example)
- Terraform Commands: `terraform init`, `terraform plan`, `terraform apply`, `terraform destroy`
- State Management (`terraform.tfstate`; remote backends like S3)

### Slide 11 — Infrastructure as Code (IaC) 🏗️
- What is Infrastructure as Code? (manage infra through code instead of manual processes)
- Why IaC is Important (repeatability, speed, auditability, disaster recovery)
- Benefits: Automation, Consistency, Version Control, Cost Reduction
- Declarative vs Imperative approach comparison table
- Tools for IaC: Terraform, Ansible, Pulumi, AWS CloudFormation, Azure Bicep
- Real-World Example: spin up a complete Kubernetes cluster on AWS EKS with 10 lines of Terraform

### Slide 12 — Python 🐍
- Why Python in DevOps? (scripting, automation, glue code, APIs)
- Data Types overview: `str`, `int`, `float`, `bool`, `list`, `dict`, `tuple`, `set`
- List example: `tools = ["Docker", "K8s", "Ansible"]`
- Dict example: `config = {"host": "localhost", "port": 3306}`
- Control Statements: `if` / `elif` / `else` with practical DevOps example
- Loops: `for` loop over servers list; `while` loop for retry logic
- Functions: `def deploy(env):` example
- Modules: `import os`, `import subprocess`, `import requests`
- Python in CI/CD Pipelines: run tests, trigger deployments, parse logs, call REST APIs

---

## 🎨 DESIGN SYSTEM

### Color Palette
```
Background:     #0d1117   (near-black)
Surface:        #161b22   (dark card)
Border:         #30363d   (subtle divider)
Text:           #e6edf3   (primary text)
Muted text:     #8b949e   (secondary text)
Accent:         #f97316   (orange — default)
Blue:           #58a6ff   (headings, links)
Cyan:           #06b6d4   (tips/info callouts)
```

### Per-Topic Accent Colors (apply to slide header border)
```
Network:    #06b6d4  (cyan)
Git/GitHub: #f43f5e  (rose)
Jenkins:    #8b5cf6  (violet)
CI/CD:      #10b981  (emerald)
Pipelines:  #eab308  (yellow)
Docker:     #3b82f6  (blue)
Kubernetes: #326ce5  (kube-blue)
Ansible:    #dc2626  (red)
Terraform:  #844FBA  (purple)
IaC:        #14b8a6  (teal)
Python:     #ca8a04  (amber)
```

### Typography
- Font: **Inter** or **Roboto** from Google Fonts
- Heading sizes: h1 `clamp(2.2rem, 5vw, 4rem)`, h2 `1.35rem`, h3 `1.05rem`
- Code font: **JetBrains Mono** or **Consolas**

### UI Components Needed
- **Slide header** with animated Google-colors flowing border line on entry
- **Navigation bar** (fixed bottom) with Prev/Next buttons and dot-indicator progress
- **Content body** with scrollable area for longer slides
- **Info callout box** (cyan left-border) for tips
- **Warning callout box** (orange left-border) for important notes
- **Two-column grid layout** for text + image/code pairs
- **Code block** with dark background (`#0d1117`) and monospace font
- **Summary card grid** (auto-fill, hover lift + glow effect)
- **Comparison table** with alternating row hover highlight
- **Key Takeaway box** (gradient orange background, amber text)

---

## 🗄️ MYSQL DATABASE SCHEMA

Create a database called `devops_presentation` with the following table:

```sql
CREATE DATABASE IF NOT EXISTS devops_presentation;
USE devops_presentation;

CREATE TABLE IF NOT EXISTS attendees (
  id            INT AUTO_INCREMENT PRIMARY KEY,
  first_name    VARCHAR(100)        NOT NULL,
  last_name     VARCHAR(100)        NOT NULL,
  email         VARCHAR(255)        NOT NULL UNIQUE,
  registered_at TIMESTAMP           DEFAULT CURRENT_TIMESTAMP
);
```

---

## 📝 ATTENDEE SIGN-UP FEATURE

### Frontend — Sign-Up Modal / Form

Trigger: A **"Register as Attendee"** button visible on the title slide and also in the navigation bar.

The modal should contain:
- **Title**: "📋 Register for This Session"
- **Subtitle**: "Save your seat — join Tim Huza's DevOps training"
- **Fields**:
  1. `First Name` (text input, required, placeholder: "John")
  2. `Last Name` (text input, required, placeholder: "Doe")
  3. `Email Address` (email input, required, placeholder: "john.doe@example.com")
- **Submit button**: "Register Now →" (orange gradient, full-width)
- **Success state**: animated checkmark + "✅ You're registered! See you at the presentation."
- **Error state**: inline error message if email already exists or server error
- **Close button**: X icon in top-right corner

### Form Validation (Client-Side)
- All fields are required (show inline red border + error message if empty on submit)
- Email must match a valid email pattern
- First and last name must be at least 2 characters
- Disable submit button while request is in flight (show spinner)

### Backend — REST API Endpoint

Create a backend API endpoint:

```
POST /api/register
Content-Type: application/json

Request Body:
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com"
}

Success Response (201):
{
  "success": true,
  "message": "Registration successful!",
  "attendee": {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "registered_at": "2026-06-03T20:00:00Z"
  }
}

Duplicate Email Response (409):
{
  "success": false,
  "message": "This email is already registered."
}

Validation Error Response (400):
{
  "success": false,
  "message": "All fields are required and must be valid."
}
```

### Backend Logic Requirements
- Sanitize and validate all inputs server-side (never trust client alone)
- Use parameterized queries / prepared statements (prevent SQL injection)
- Hash or trim whitespace from inputs before storing
- Return appropriate HTTP status codes (201 Created, 400 Bad Request, 409 Conflict, 500 Internal Server Error)
- Log each successful registration with timestamp

---

## 🧭 NAVIGATION & UX

- **Keyboard navigation**: `ArrowRight` / `ArrowDown` → next slide; `ArrowLeft` / `ArrowUp` → previous slide
- **Dot indicators**: clickable dot per slide, active dot highlighted in accent color
- **Counter**: "3 / 45" style slide counter in the nav bar
- **Prev/Next buttons**: disabled when at first/last slide
- **Smooth slide transitions**: fade-in animation on slide change
- **Scroll reset**: scroll body back to top when changing slides
- **Mobile responsive**: stack two-column layouts on viewports < 700px
- **Register button** always visible in nav bar (fixed bottom-right corner)

---

## 🏗️ TECHNICAL STACK REQUIREMENTS

| Layer       | Technology         |
|-------------|-------------------|
| Frontend    | HTML5, CSS3 (Vanilla), JavaScript (ES6+) |
| Backend     | Node.js (Express.js) OR Python (FastAPI / Flask) |
| Database    | MySQL 8.x |
| DB Client   | `mysql2` (Node.js) OR `pymysql` / `aiomysql` (Python) |
| Environment | `.env` file for DB credentials |

### Environment Variables (`.env`)
```
DB_HOST=localhost
DB_PORT=3306
DB_USER=devops_user
DB_PASSWORD=yourSecurePassword
DB_NAME=devops_presentation
```

---

## 📁 SUGGESTED FILE STRUCTURE

```
devops-presentation/
├── public/
│   ├── index.html          ← Main presentation HTML
│   ├── style.css           ← All styles (dark theme, components)
│   ├── app.js              ← Slide navigation + modal logic
│   └── static/
│       └── images/         ← Tool logos (Docker, K8s, Ansible, etc.)
├── server/
│   ├── index.js            ← Express server entry point
│   ├── routes/
│   │   └── register.js     ← POST /api/register route handler
│   ├── db/
│   │   ├── connection.js   ← MySQL connection pool
│   │   └── schema.sql      ← Database schema (DDL)
│   └── middleware/
│       └── validate.js     ← Input validation middleware
├── .env                    ← DB credentials (not committed to Git)
├── .gitignore              ← node_modules, .env
├── package.json
└── README.md               ← Setup instructions
```

---

## ✅ ACCEPTANCE CRITERIA

1. **Presentation loads** and all 13 sections are fully navigable
2. **Title slide** displays correctly with hero design and "Register" CTA
3. **All content** from the outline above is included and well-formatted
4. **Register button** opens an animated modal with the three-field form
5. **Form validates** client-side before submission
6. **Submission calls** the `/api/register` endpoint with POST
7. **MySQL records** are correctly saved to the `attendees` table
8. **Duplicate email** returns a clear, user-friendly error message
9. **Success state** shows confirmation animation after registration
10. **Navigation** works via buttons, dots, and keyboard arrows
11. **Design** matches the dark-theme DevOps aesthetic described above
12. **Mobile** layout is responsive and usable on smaller screens
13. **Code is clean**, well-commented, and follows best practices
14. **SQL injection** is prevented via parameterized queries
15. **README** includes clear setup steps for the MySQL database and server

---

## 🚀 SETUP INSTRUCTIONS TO INCLUDE IN README

The generated README should instruct the user to:

1. Install Node.js (v18+) and MySQL 8.x
2. Create the MySQL database and user:
   ```sql
   CREATE DATABASE devops_presentation;
   CREATE USER 'devops_user'@'localhost' IDENTIFIED BY 'yourPassword';
   GRANT ALL PRIVILEGES ON devops_presentation.* TO 'devops_user'@'localhost';
   FLUSH PRIVILEGES;
   ```
3. Run `schema.sql` to create the `attendees` table
4. Copy `.env.example` to `.env` and fill in credentials
5. Run `npm install` and `npm start`
6. Open `http://localhost:3000` in the browser

---

*This prompt was authored for use with Google Stitch to generate a full-stack DevOps presentation app.*
*Presentation content by Tim Huza — DevOps Instructor.*
