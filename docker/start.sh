#!/bin/bash

# Prüfen ob .env angelegt wurde
if [[ ! -s ../backend/.env ]]; then
    echo "Fehler: Datei .env nicht angelegt"
    exit 1
fi

docker compose --env-file ../backend/.env -f compose.yaml down -v
docker compose --env-file ../backend/.env -f compose.yaml up --build -d --wait
docker compose --env-file ../backend/.env -f compose.yaml exec -T backend python -m src.database_operations.create.create_database
docker compose --env-file ../backend/.env -f compose.yaml exec -T backend python -m src.database_operations.initialize.initialize_database
docker compose --env-file ../backend/.env -f compose.yaml up
