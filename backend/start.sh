#!/bin/bash

# Prüfen ob .env angelegt wurde
if [[ ! -s .env ]]; then
    echo "Fehler: Datei .env nicht angelegt"
    exit 1
fi

docker compose down -v
docker compose up --build -d # -d macht detached, damit die scripte danach laufen

docker exec pwe-backend python -m src.database_operations.create.create_database
docker exec pwe-backend python -m src.database_operations.initialize.initialize_database

docker compose up # ohne zusatz Argumente, dockt an laufende session an