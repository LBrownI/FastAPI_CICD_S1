# FastAPI_CICD_S1

[![Build and Push Docker Image](https://github.com/LBrownI/FastAPI_CICD_S1/actions/workflows/build-and-push.yml/badge.svg)](https://github.com/LBrownI/FastAPI_CICD_S1/actions/workflows/build-and-push.yml)
[![Test and Lint](https://github.com/LBrownI/FastAPI_CICD_S1/actions/workflows/test-and-lint.yml/badge.svg)](https://github.com/LBrownI/FastAPI_CICD_S1/actions/workflows/test-and-lint.yml)

[![Docker Image](https://img.shields.io/docker/v/lbrowni/fastapi-app?label=Docker%20Image&sort=semver)](https://hub.docker.com/r/lbrowni/fastapi-app)
[![Docker Size](https://img.shields.io/docker/image-size/lbrowni/fastapi-app/latest)](https://hub.docker.com/r/lbrowni/fastapi-app)
[![Docker Pulls](https://img.shields.io/docker/pulls/lbrowni/fastapi-app)](https://hub.docker.com/r/lbrowni/fastapi-app)

[![Python Version](https://img.shields.io/badge/python-3.12-green.svg)](https://www.python.org/downloads/release/python-3120/)
[![FastAPI Version](https://img.shields.io/badge/FastAPI-0.115.12-darkgreen.svg)](https://fastapi.tiangolo.com/)
[![Poetry Version](https://img.shields.io/badge/Poetry-2.1.2-darkblue.svg)](https://python-poetry.org/)
[![Pytest Version](https://img.shields.io/badge/Pytest-8.3.5-lightgreen.svg)](https://docs.pytest.org/en/stable/)

## Description

FastAPI_CICD_S1 is a web application developed with FastAPI that serves as an example for continuous integration and continuous delivery (CI/CD) using GitHub Actions. The application includes a couple of basic endpoints to demonstrate API functionality, automated testing, and deployment using Docker.

## Features

- Simple endpoints:

  - GET /: Returns a greeting message.

  - GET /time: Returns the current server date and time in the format _`YYYY-MM-DD HH:MM:SS`_.

- **Dependency Management**:

  Poetry is used to manage dependencies and project configuration.
  A `requirements.txt` file is also included for compatibility with pip-based environments.

- **Testing**:

  Tests are implemented using pytest and validate endpoints (e.g., the date format in /time).

- **CI/CD**:

  Integration with GitHub Actions automates test execution, code linting with flake8, and Docker image build/push.

- **Containerization**:

  A Dockerfile is included to build the application image, making deployment in containers easier.

## Requirements

- Python: Version 3.12 or higher.

- Poetry: For dependency management.

- Docker: (Optional) To run the application in a container.

- Pip: If you prefer to use the requirements.txt file to install dependencies.

## Deployment Options (DockerHub or GitHub)

## Option 1: DockerHub (recommended)

If you have Docker Desktop (or another Docker runtime) running, the fastest way is to pull and run the pre-built image from Docker Hub:

1. **Pull the image:**
   ```bash
   docker pull lbrowni/fastapi-app:latest
   ```
2. **Run the container:**
   ```bash
   docker run -p 8000:8000 lbrowni/fastapi-app:latest
   ```
3. **Access the application:** Open your browser and navigate to http://0.0.0.0:8000/ to test the API

## Option 2: GitHub (Installation & Local Setup)

You can also clone the repository, install dependencies, and run the app locally.

1. Clone the repository:

```
git clone https://github.com/LBrownI/FastAPI_CICD_S1.git
cd FastAPI_CICD_S1
```

2. Install dependencies:

```
poetry install
```

## Usage

### Run the Application

Start the app using uvicorn:

```
uvicorn app.main:app --reload
```

## Available Endpoints

- **GET /**: Returns:
  ```
    {
        "Hello": "World"
    }
  ```
- **GET /time**: Returns the current date and time:
  ```
    "current_time": "2023-10-01 12:00:00"
  ```

## Testing

The project includes automated tests using pytest. To run the tests, use the following command:

```
poetry run pytest
```

## Continuous Integration and Continuous Delivery (CI/CD)

The project includes a GitHub Actions workflow that performs the following tasks:

- **Checkout:** Pulls the code from the repository.
- **Python Setup:** Configures the Python environment (3.12).
- **Poetry Installation and Dependency Setup**
- **Linting Execution:** Runs flake8 to analyze the code.
- **Test Execution:** Runs pytest to validate the application functionality.
- **Docker Build:** Once tests and linting pass, builds the Docker image of the application and pushes it to Docker Hub (requires configuring `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN`).

## Containerization with Docker

The included `Dockerfile` allows building an image of the application. To build and run the image, use the following commands:

1. Build the image:

```
docker build -t fastapi-app .
```

2. Run the container:

```
docker run -d -p 8000:8000 fastapi-app
```

## Extra info

- DOCKERHUB REPOSITORY: you can access the repo at https://hub.docker.com/r/lbrowni/fastapi-app or by searching the repository on dockerhub with lbrowni/fastapi-app.
- GITHUB REPOSITORY: if you are reading this from a local folder and would like to see how the banners look check out: https://github.com/LBrownI/FastAPI_CICD_S1
