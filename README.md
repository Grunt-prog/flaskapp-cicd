# 🚀 Flask App with CI/CD using Jenkins

This is a basic Flask application integrated with **Jenkins CI/CD pipeline**. Any change pushed to the repository triggers Jenkins to automatically build and deploy the application.

---

## 🧱 Tech Stack

- **Flask** – Python web framework
- **Jenkins** – Continuous Integration and Deployment
- **Docker** – Containerized deployment (if applicable)

---

## 📁 Features

- Simple Flask web app
- Jenkins pipeline integration
- Auto-deploy on repository changes

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Grunt-prog/flaskapp-cicd.git
cd flaskapp-cicd
```

### 2. Run the App Locally (optional)

```bash
pip install -r requirements.txt
python app.py
```

Then go to:

```
http://localhost:5000
```

---

## ⚙️ CI/CD with Jenkins

- A Jenkins job (freestyle or pipeline) is set up to monitor this GitHub repo.
- When changes are pushed:
  - Jenkins pulls the latest code
  - Builds the project (if necessary)
  - Deploys or runs it automatically

> Make sure Jenkins has Git and Python configured and that webhook (or polling) is enabled for this repo.

---

## 📜 License

MIT License
