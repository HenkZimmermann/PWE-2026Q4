from fastapi import FastAPI
from src.sections.groups import groups_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(groups_routes.router)

@app.get("/")
def root():
    return {"message": "FastAPI läuft"}