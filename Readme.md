# IMC App Docker

A simple BMI (IMC) calculator web application, containerized with Docker for easy deployment.

## Features

- Calculate Body Mass Index (BMI/IMC)
- Responsive web interface
- Easy to run locally or deploy with Docker

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/imc-app-docker.git
cd imc-app-docker
```

### 2. Deploy using docker-compose

```bash
docker compose up --build
```

### 3. Deploy with kubernetes

```bash
kubectl apply -f ./k8s/base/
```

The app will be available at [http://localhost:8080](http://localhost:8080).

## Project Structure

```
imc-app-docker/
├── backend/                # Application source code
├── frontend/                # Application source code
├── k8s/
└── Readme.md
└── docker-compose.yml
└── Readme.md
```

## License

This project is licensed under the MIT License.