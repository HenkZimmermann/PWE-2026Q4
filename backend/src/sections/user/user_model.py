from pydantic import BaseModel, EmailStr

class CreateRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    role_id: str

class LoginRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

class EditRequest(BaseModel):
    username: str
    email: EmailStr
    role_id: str