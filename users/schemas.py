from pydantic import BaseModel


class UserSchema(BaseModel):
    user_name: str
    password: str
    role: str


class PartialUserSchema(BaseModel):
    password: str | None = None
    user_name: str
