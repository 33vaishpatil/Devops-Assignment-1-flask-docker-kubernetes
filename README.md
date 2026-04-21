# DEVOPS_ASSIGNMENT

## Assignment-1:

```
Task 1: End-to-End Docker and Kubernetes Deployment

In this task, you need to take a simple web application (Node.js or Python Flask) 
and deploy it using Docker and Kubernetes. The goal is to understand how an 
application moves from local development to a container and then into a Kubernetes cluster.

You will start by creating a basic application that runs locally and responds on a specific port. 
Once it works, you must containerise it using Docker.

Write a proper Dockerfile using a lightweight base image and build the Docker image locally. 
Run the container and confirm it works correctly.

After that, push the Docker image to Docker Hub or GitLab Container Registry. 
Using Minikube or Kind, deploy the same image into Kubernetes.

Your implementation must include:

- A working application
- Dockerfile and .dockerignore
- Image build and push to registry
- Kubernetes Deployment YAML
- Kubernetes Service YAML
- Scaling replicas from 1 to 3
- Performing a rolling update by changing image version (v1 → v2)
```

You should also provide a short explanation covering:

- What happens when a pod crashes?
- Difference between Pod and Deployment
- Purpose of a Service in Kubernetes
- How rolling updates work
