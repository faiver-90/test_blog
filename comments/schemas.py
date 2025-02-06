from pydantic import BaseModel


class CommentSchema(BaseModel):
    content: str


class CommentResponseSchema(BaseModel):
    id: int
    content: str
    author_id: int
    article_id: int
