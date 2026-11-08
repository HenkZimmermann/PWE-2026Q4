from fastapi import FastAPI
from src.sections.groups import groups_routes
from src.sections.role import role_routes
from src.sections.comment import comment_routes
from src.sections.thread import thread_routes
from src.sections.follows import follows_routes
from src.sections.member_of import member_of_routes
from src.sections.vote import vote_routes
from src.sections.user import user_routes
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
app.include_router(role_routes.router)
app.include_router(comment_routes.router)
app.include_router(thread_routes.router)
app.include_router(follows_routes.router)
app.include_router(member_of_routes.router)
app.include_router(vote_routes.router)
app.include_router(user_routes.router)

@app.get("/")
def root():
    return {"message": "FastAPI läuft"}