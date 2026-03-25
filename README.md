# Python URL Shortener

![Python](https://img.shields.io/badge/python-3.11-blue)
![Docker](https://img.shields.io/badge/docker-containerized-blue)
![Kubernetes](https://img.shields.io/badge/kubernetes-deployed-blue)
![GCP](https://img.shields.io/badge/google%20cloud-GCP-blue)
![Terraform](https://img.shields.io/badge/terraform-infrastructure-purple)
![License](https://img.shields.io/badge/license-MIT-green)

A simple URL shortening service built with Python and deployed on Kubernetes.

This project demonstrates a full DevOps workflow including containerization, infrastructure provisioning, monitoring, and automated deployment.

Repository:  
https://github.com/sassenagh/python-url-shortener

---

# Architecture

The application runs as a containerized service deployed to Kubernetes on Google Cloud.

```
             ┌───────────────┐
             │     User      │
             └───────┬───────┘
                     │
                     ▼
           Kubernetes LoadBalancer
                     │
                     ▼
            Python URL Shortener API
                     │
                     ▼
                  Redis
             (URL persistence)
                     │
                     ▼
      ┌──────────────┴──────────────┐
      ▼                             ▼
  Prometheus                     Grafana
 (metrics)                     (dashboards)
```

Deployment workflow:

```
GitHub → CI/CD → Docker Image → Artifact Registry → GKE
```

---

# Features

- URL shortening service
- Redirect shortened URLs to original links
- Redis-based storage
- Health and readiness probes
- Containerized with Docker
- Kubernetes deployment
- Infrastructure as Code with Terraform
- Monitoring with Prometheus
- Visualization with Grafana
- CI/CD pipeline with GitHub Actions

---

# Tech Stack

## Backend

- Python
- FastAPI

## Infrastructure

- Docker
- Kubernetes
- Terraform

## Cloud

- Google Cloud
- Google Kubernetes Engine (GKE)
- Artifact Registry

## Observability

- Prometheus
- Grafana

## CI/CD

- GitHub Actions

---

# Project Structure

```
python-url-shortener
│
├── app
│   ├── main.py
│   ├── routes
│   ├── services
│   └── redis_client.py
│
├── infrastructure
│   ├── terraform
│   │   └── gke.tf
│   │
│   └── k8s
│       ├── deployment.yaml
│       ├── service.yaml
│       ├── prometheus.yaml
│       └── grafana.yaml
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# API Endpoints

## Create Short URL

```
POST /shorten
```

Request body:

```json
{
  "url": "https://example.com/some/very/long/url"
}
```

Response:

```json
{
  "short_url": "http://localhost:8000/abc123"
}
```

---

## Redirect to Original URL

```
GET /{short_code}
```

Example:

```
GET /abc123
```

This redirects to the original stored URL.

---

## Health Check

```
GET /health
```

Used by Kubernetes liveness probe.

---

## Readiness Check

```
GET /ready
```

Used by Kubernetes readiness probe.

---

# Running Locally

Clone the repository:

```bash
git clone https://github.com/sassenagh/python-url-shortener.git
cd python-url-shortener
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app/main.py
```

The API will be available at:

```
http://localhost:8000
```

---

# Running with Docker

Build the image:

```bash
docker build -t python-url-shortener .
```

Run the container:

```bash
docker run -p 8000:8000 python-url-shortener
```

---

# Deployment

Infrastructure is provisioned with Terraform and deployed to Kubernetes.

Provision infrastructure:

```bash
terraform init
terraform apply
```

Deploy the application:

```bash
kubectl apply -f infrastructure/k8s
```

Check running pods:

```bash
kubectl get pods -A
```

---

# Monitoring

The project includes a monitoring stack.

## Prometheus

```
http://<PROMETHEUS-IP>:9090
```

## Grafana

```
http://<GRAFANA-IP>:3000
```

Default credentials:

```
admin / admin
```

---

# CI/CD Pipeline

The CI/CD pipeline automatically:

1. Builds the Docker image
2. Pushes it to Artifact Registry
3. Deploys the application to Kubernetes

Implemented with GitHub Actions.

---

# Future Improvements

- Rate limiting
- Custom short URLs
- Expiration for links
- Click analytics
- Authentication for link management
- Helm charts for deployment
- Horizontal pod autoscaling

---

# License

MIT License