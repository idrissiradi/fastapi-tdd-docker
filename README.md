# Test-Driven Development with FastAPI and Docker

A FastAPI service backed by PostgreSQL and Tortoise ORM.

![Continuous Integration and Delivery](https://github.com/idrissiradi/fastapi-tdd-docker/actions/workflows/main.yml/badge.svg?branch=main)

## Run with Docker Compose

Start the API and PostgreSQL containers from the repository root:

```bash
docker compose up --build -d
```

Apply the database migrations before creating summaries:

```bash
docker compose exec web aerich upgrade
```

Check that the API is responding at <http://localhost:8004/ping>. Interactive API documentation is available at <http://localhost:8004/docs>.

Create a summary with:

```bash
curl -X POST http://localhost:8004/summaries/ \\
  -H 'Content-Type: application/json' \\
  -d '{"url":"https://testdriven.io"}'
```

Run the test suite inside the web container with:

```bash
docker compose exec web python -m pytest
```

Stop the containers with `docker compose down`.
