from ninja import Router

from auth_custom.sercvices.jwt_service import JWTAuth
from comments.coments_services import CommentService
from comments.schemas import CommentResponseSchema, CommentSchema

comments_router = Router(tags=['Comments'])
comment_service = CommentService()


@comments_router.post("/create_comment/{article_id}", response=CommentResponseSchema, auth=JWTAuth())
def create_comment(request, article_id: int, data: CommentSchema):
    comment = comment_service.create_comment(request.auth["user_id"], article_id, data.content)
    return comment


@comments_router.put("/update_comment/{comment_id}", response=CommentResponseSchema, auth=JWTAuth())
def update_comment(request, comment_id: int, data: CommentSchema):
    comment = comment_service.update_comment(comment_id, request.auth["user_id"], data.content)
    if not comment:
        return {"detail": "Permission denied"}
    return comment


@comments_router.delete("/delete_comment/{comment_id}", auth=JWTAuth())
def delete_comment(request, comment_id: int):
    success = comment_service.delete_comment(comment_id, request.auth["user_id"])
    if not success:
        return {"detail": "Permission denied"}, 403
    return {"message": "Comment deleted successfully"}


@comments_router.get("/get_comments/{article_id}", response=list[CommentResponseSchema], auth=JWTAuth())
def get_comments(request, article_id: int):
    return comment_service.get_comments_by_article(article_id)
