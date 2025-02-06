from pydantic import BaseModel


class ArticleSchema(BaseModel):
    title: str
    content: str
    category_id: int


class ArticleResponseSchema(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    category_id: int
