# 🎯 Terraform

## 🛠️ What is Terraform?

Terraform is a tool used to **build and manage infrastructure using code**.

* Created by HashiCorp
* Works with cloud providers (AWS, Azure, GCP)
* Uses `.tf` configuration files

💡 One of the most popular IaC tools

---

## 🔌 Providers in Terraform

Providers allow Terraform to interact with platforms:

* AWS
* Azure
* Google Cloud

Example:
```hcl
provider "aws" {
  region = "us-east-1"
}
```

## 🧱 Basic Terraform Configuration

Terraform uses simple configuration blocks:

```hcl
resource "aws_instance" "example" {
  ami           = "ami-123456"
  instance_type = "t2.micro"
}
```

💡 This creates a virtual machine in the cloud

---

## ⚙️ Terraform Commands

| Command           | Purpose            |
| ----------------- | ------------------ |
| `terraform init`  | Initialize project |
| `terraform plan`  | Preview changes    |
| `terraform apply` | Apply changes      |

💡 Always run `plan` before `apply`!