docker compose down -v
docker compose up --build -d
docker exec pwe-backend python src/database_operations/create/create_database.py
docker exec pwe-backend python src/database_operations/initialize/initialize_database.py