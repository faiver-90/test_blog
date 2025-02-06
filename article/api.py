from ninja import Router

from article.article_services import ArticleService
from article.schemas import ArticleResponseSchema, ArticleSchema
from auth_custom.sercvices.jwt_service import JWTAuth

article_router = Router()
article_service = ArticleService()


@article_router.post("/articles", response=ArticleResponseSchema, auth=JWTAuth())
def create_article(request, data: ArticleSchema):
    article = article_service.create_article(request.auth["user_id"], data)
    return article


@article_router.put("/articles/{article_id}", response=ArticleResponseSchema, auth=JWTAuth())
def update_article(request, article_id: int, data: ArticleSchema):
    article = article_service.update_article(article_id, request.auth["user_id"], data)
    if not article:
        return {"detail": "Permission denied"}, 403
    return article


@article_router.delete("/articles/{article_id}", auth=JWTAuth())
def delete_article(request, article_id: int):
    success = article_service.delete_article(article_id, request.auth["user_id"])
    if not success:
        return {"detail": "Permission denied"}, 403
    return {"message": "Article deleted successfully"}


@article_router.get("/articles/{article_id}", response=ArticleResponseSchema)
def get_article(request, article_id: int):
    return article_service.get_article_by_id(article_id)
