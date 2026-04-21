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

You should also provide a short explanation covering:

- What happens when a pod crashes?
- Difference between Pod and Deployment
- Purpose of a Service in Kubernetes
- How rolling updates work
```
### Solution

For Task 1, a complete end-to-end deployment of a Python Flask web application was successfully implemented using Docker and Kubernetes.

A Flask application was created and tested locally on port **5000**. After successful execution, the application was containerized using Docker by creating a proper `Dockerfile` and `.dockerignore` file using a lightweight base image.

The Docker image was built locally, tested through a running container, and then pushed to Docker Hub for registry access.

Using Minikube, a local Kubernetes cluster was created. The same Docker image was deployed into Kubernetes using Deployment and Service YAML files.

The application was successfully accessed through Kubernetes, replicas were scaled from **1 to 3**, and a rolling update was performed by changing the image version from **v1 to v2**.

All required objectives of Task 1 were successfully completed.

---

### Steps

#### 1. Application Development

- Created a Python Flask web application.
- Configured application to run on port **5000**.
- Verified locally using:

```text
http://127.0.0.1:5000/
