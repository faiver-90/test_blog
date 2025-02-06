from ninja import Router

from auth_custom.sercvices.jwt_service import JWTAuth
from comments.coments_services import CommentService
from comments.schemas import CommentResponseSchema, CommentSchema

comments_router = Router()
comment_service = CommentService()


# 🔹 Создание комментария
@comments_router.post("/articles/{article_id}/comments", response=CommentResponseSchema, auth=JWTAuth())
def create_comment(request, article_id: int, data: CommentSchema):
    comment = comment_service.create_comment(request.auth["user_id"], article_id, data.content)
    return comment


# 🔹 Обновление комментария (только автор или админ)
@comments_router.put("/comments/{comment_id}", response=CommentResponseSchema, auth=JWTAuth())
def update_comment(request, comment_id: int, data: CommentSchema):
    comment = comment_service.update_comment(comment_id, request.auth["user_id"], data.content)
    if not comment:
        return {"detail": "Permission denied"}, 403
    return comment


# 🔹 Удаление комментария (только автор или админ)
@comments_router.delete("/comments/{comment_id}", auth=JWTAuth())
def delete_comment(request, comment_id: int):
    success = comment_service.delete_comment(comment_id, request.auth["user_id"])
    if not success:
        return {"detail": "Permission denied"}, 403
    return {"message": "Comment deleted successfully"}


# 🔹 Получение всех комментариев к статье
@comments_router.get("/articles/{article_id}/comments", response=list[CommentResponseSchema])
def get_comments(request, article_id: int):
    return comment_service.get_comments_by_article(article_id)
