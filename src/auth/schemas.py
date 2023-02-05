from pydantic import BaseModel

class Role(BaseModel):
    id: int
    role: str


class User(BaseModel):
    id: int
    email: str
    username: str
    # password: str
    name: str
    surname: str
    role_id: int


class UserPatch(BaseModel):
    email: str = None
    username: str = None
    password: str = None
    name: str = None
    surname: str = None
    role_id: int = None


class UserLogin(BaseModel):
    email: str
    password: str