User-Feedback-App - Two-Tier Application (DevOps Project)
📘 Overview

This project is a Simplified Two-Tier Application built as part of a DevOps learning journey. It demonstrates how to >

The two-tier setup consists of:

Backend – a Flask-based REST API

Frontend – a simple JavaScript-based web interface that communicates with the backend API

🧩 Architecture

The application follows a two-tier architecture:

Frontend Tier – Handles user interaction through a web page.

Backend Tier – Processes data and handles API requests.

Both tiers are containerized and connected via a custom Docker network for seamless communication.

Browser → Frontend (Container) → Backend (Container)

⚙️ Phase-by-Phase Implementation
Phase 1: Project Setup

Created project directories:
simplified-two-tier-app/
├── backend/
├── frontend/
├── docker-compose.yml


Initialized a basic Flask backend (app.py) to handle API requests.

Added a simple HTML/JavaScript frontend that sends a POST request to the backend API.

Phase 2: Dockerization

Added Dockerfiles for both the frontend and backend.

Added .dockerignore for both the frontend and backend as well to avoid unnecessary files included in the build.

Backend Dockerfile included:

Base image: python:3.11-slim

Installed dependencies from requirements.txt

Exposed port 5000

Used a non-root user (node:node) and created /app/data directory with proper permissions.

Frontend Dockerfile included:

Base image: nginx:alpine

Installed necessary npm packages.

Exposed port 80

Built images using:

docker build -t my-frontend ./frontend
docker build -t my-backend ./backend

Phase 3: Docker Compose Integration

Created a docker-compose.yml file to define and orchestrate both services:

version: '3.8'

services:
  backend:
    build: ./backend
    container_name: backend
    ports:
      - "5000:5000"
    networks:
      - app-network

  frontend:
    build: ./frontend
    container_name: frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
    networks:
      - app-network

networks:
  app-network:
    driver: bridge


Verified that both containers run together using:

docker-compose up --build

Confirmed successful communication between containers inside the Docker network.

🧪 How to Run the Project
1. Clone the Repository
git clone <your repo dir>
cd simplified-two-tier-app

2. Build and Start Containers
docker-compose up --build

3. Access the App

Frontend: http://localhost:8080

Backend API: http://localhost:5000

🧰 Tech Stack
Layer   Technology
Frontend        HTML, JavaScript
Backend Python (Flask)
Containerization        Docker, Docker Compose
Networking      Bridge Network
🚀 Next Steps (Upcoming Phases)

Implement persistent data storage using Docker volumes.

Integrate a lightweight database (e.g., SQLite or PostgreSQL).

Add CI/CD pipeline with GitHub Actions or Jenkins.

Introduce automated testing and environment variables management.

👨‍💻 Author

Yomi Olowu
DevOps Enthusiast | Technology Consultant @ Accede
