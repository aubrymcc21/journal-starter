# Journal App

A journaling FastAPI web app deployed with Docker and monitored using Prometheus and Grafana. This project is part of the Learn To Cloud capstone.

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **Containerization**: Docker + Docker Compose
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus + Grafana

## Running Locally

1. Create a `.env` file in the root to store the DATABASE_URL variable. It will look something like postgresql://youruser:yourpass@yourhost:5432/yourdb.

2. Start services:

```bash
docker-compose up --build

3. Visit:
- FastAPI: http://localhost:8000/docs
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

## 4. **CI/CD Pipeline**

```markdown
## CI/CD Pipeline

- On push to `main`, GitHub Actions:
  - Installs dependencies
  - (Optional) Runs tests
  - Builds Docker image
  - Pushes to Azure Container Registry (ACR)

## Kubernetes Deployment

- Kubernetes manifests located in `/k8s` (if you created them).
- Deploy with:

```bash
kubectl apply -f k8s/

## ✅ 6. **Monitoring Dashboards**

```markdown
### Monitoring with Grafana

- Prometheus scrapes `/metrics` from FastAPI every 15s.
- Grafana visualizes:
  - Total requests
  - Request latency
  - Error rates

Dashboard setup steps:
1. Add Prometheus as a data source (http://prometheus:9090).
2. Create dashboard with PromQL queries like: http_requests_total
