# CI/CD Pipeline with GitHub Actions, Docker, Kubernetes, and AWS EKS

This repository contains the configuration and setup for a **CI/CD pipeline** that automates the process of building, testing, and deploying Dockerised applications to an AWS EKS (Elastic Kubernetes Service) cluster. This setup ensures that applications are continuously integrated and deployed efficiently and securely.

## 🚀 Overview

The CI/CD pipeline automates the following processes:

- **Build Docker Images**: Create Docker images for applications.
- **Push Images to Docker Hub**: Upload the built images to a Docker repository.
- **Security Scanning**: Scan images for vulnerabilities.
- **Deploy to AWS EKS**: Deploy the Docker images to a Kubernetes cluster on AWS EKS.
- **Monitoring Setup (Optional)**: Configure monitoring tools such as Prometheus and Grafana.

## 🔄 Pipeline Workflow

The pipeline is defined using GitHub Actions and includes the following key steps:

### 1. Build and Push Docker Images

- **Log in to Docker Hub**: Authenticate using stored credentials.
- **Build Images**: Create Docker images for both the application and web frontend.
- **Push Images**: Upload the images to Docker Hub.

### 2. Security Scanning

- **Scan Images**: Use [Trivy](https://github.com/aquasecurity/trivy) to identify vulnerabilities in the Docker images.

### 3. Deploy to AWS EKS

- **Configure AWS Credentials**: Set up AWS access for deployment.
- **Update kubeconfig**: Point to the EKS cluster.
- **Deploy**: Apply Kubernetes manifests to deploy the images.

### 4. Monitoring Setup (Optional)

- **Install Helm**: Package manager for Kubernetes.
- **Deploy Monitoring Tools**: Install Prometheus and Grafana using Helm.

## 🛠️ Getting Started

### Prerequisites

- **GitHub Repository**: Ensure your code is hosted on GitHub.
- **Docker**: Docker installed locally for testing.
- **AWS EKS**: An active AWS EKS cluster.
- **Docker Hub Account**: For storing and retrieving Docker images.
- **GitHub Secrets**: Set up secrets for Docker Hub and AWS credentials.

### Setup Instructions

1. **Configure GitHub Secrets**:
   - Navigate to the repository settings on GitHub.
   - Add secrets for `DOCKERHUB_USERNAME`, `DOCKERHUB_PASSWORD`, `AWS_ACCESS_KEY_ID`, and `AWS_SECRET_ACCESS_KEY`.

2. **Add GitHub Actions Workflow**:
   - Create a `.github/workflows/ci-cd-pipeline.yml` file in your repository.
   - Copy and modify the provided workflow YAML file to suit your project structure.

3. **Ensure Dockerfile Accuracy**:
   - Verify that your `Dockerfile` is correctly configured for your application.

4. **Commit and Push**:
   - Commit your changes and push to the `master` branch to trigger the pipeline.

## 🐞 Troubleshooting

- **Image Not Found**: Ensure Docker images are tagged correctly and match the expected names.
- **Build Failures**: Check Dockerfile paths and dependencies.
- **Deployment Issues**: Verify AWS credentials and Kubernetes configurations.

## 💡 Additional Tips

- **Modular Configuration**: Keep YAML configurations flexible to adapt to changes in cloud environments.
- **Security**: Regularly scan images for vulnerabilities to maintain a secure deployment environment.
- **Caching**: Use caching to speed up builds and reduce resource consumption.

## 🤝 Contributing

Feel free to submit issues or pull requests to improve this CI/CD pipeline setup.

