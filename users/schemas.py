from pydantic import BaseModel


class UserSchema(BaseModel):
    user_name: str
    password: str


class PartialUserSchema(BaseModel):
    password: str | None = None
