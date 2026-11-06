from fastapi import FastAPI
from sections.groups import groups_routes
from sections.role import role_routes
from sections.comment import comment_routes
from sections.thread import thread_routes
from sections.follows import follows_routes
from sections.member_of import member_of_routes
from sections.vote import vote_routes
from sections.user import user_routes
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