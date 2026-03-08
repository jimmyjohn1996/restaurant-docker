# 🍽️ Saffron & Sage — Dockerized Restaurant Website

A production-ready containerized web application deployed on AWS with a fully automated CI/CD pipeline.

## 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| Docker | Containerization |
| nginx | Web server |
| AWS EC2 | Cloud hosting |
| AWS ALB | Load balancing |
| GitHub Actions | CI/CD pipeline |
| Docker Hub | Image registry |

## 📐 Architecture

```
Developer
    │
    │  git push
    ▼
GitHub (source code)
    │
    │  triggers automatically
    ▼
GitHub Actions (CI/CD)
    │
    ├── Build Docker image
    └── Push to Docker Hub
            │
            │  docker pull
            ▼
        AWS EC2
            │
            │
        nginx container
            │
            ▼
        Live Website
```

## ⚙️ CI/CD Pipeline

Every push to `main` branch automatically:
1. Builds a new Docker image
2. Tags it with `latest` and a version number
3. Pushes it to Docker Hub

## 🐳 Docker Hub

Image available at:
```
docker pull dockerimagesaws/saffron-sage:latest
```

## 🏃 Run Locally

```bash
# Clone the repo
git clone https://github.com/jimmyjohn1996/restaurant-docker.git
cd restaurant-docker

# Build the image
docker build -t saffron-sage .

# Run the container
docker run -d -p 80:80 saffron-sage

# Open in browser
http://localhost
```

## 📁 Project Structure

```
restaurant-docker/
├── index.html          # Main website (HTML/CSS/JS)
├── images/             # Static assets
├── Dockerfile          # Container configuration
└── .github/
    └── workflows/
        └── deploy.yml  # GitHub Actions CI/CD pipeline
```

## 📝 What I Learned

- Writing and optimizing Dockerfiles
- Serving static sites with nginx in containers
- Deploying containers on AWS EC2
- Setting up Application Load Balancers on AWS
- Building CI/CD pipelines with GitHub Actions
- Managing Docker images on Docker Hub
- Transferring files to EC2 using SCP
- Linux commands on Amazon Linux 2023
