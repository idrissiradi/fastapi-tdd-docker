# FastAPI TDD Docker

A FastAPI service backed by PostgreSQL and Tortoise ORM.

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
