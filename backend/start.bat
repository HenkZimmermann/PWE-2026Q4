docker compose down -v
docker compose up --build -d
docker exec pwe-backend python -m src.database_operations.create.create_database
docker exec pwe-backend python -m src.database_operations.initialize.initialize_database