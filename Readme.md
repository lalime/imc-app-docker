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

### 2. Build the Docker image

```bash
docker build -t imc-app .
```

### 3. Run the container

```bash
docker run -p 8080:80 imc-app
```

The app will be available at [http://localhost:8080](http://localhost:8080).

## Project Structure

```
imc-app-docker/
├── src/                # Application source code
├── Dockerfile
└── Readme.md
```

## License

This project is licensed under the MIT License.