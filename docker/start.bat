::Prüfen ob .env angelegt wurde
if not exist "..\backend\.env" (
    echo Fehler: Datei .env nicht angelegt
    exit /b 1
)
docker compose --env-file ../backend/.env -f compose.yaml down -v
docker compose --env-file ../backend/.env -f compose.yaml up --build -d --wait
docker compose --env-file ../backend/.env -f compose.yaml exec -T backend python -m src.database_operations.create.create_database
docker compose --env-file ../backend/.env -f compose.yaml exec -T backend python -m src.database_operations.initialize.initialize_database
docker compose --env-file ../backend/.env -f compose.yaml up 
