from ninja import NinjaAPI, Router

from article.api import article_router
from auth_custom.api import auth_router
from auth_custom.sercvices.jwt_service import JWTAuth
from comments.api import comments_router
from users.schemas import UserSchema, PartialUserSchema
from users.user_service import UserService

api = NinjaAPI()

user_router = Router(tags=['Users'])

api.add_router('/auth', auth_router)
api.add_router('/user', user_router)
api.add_router('/article', article_router)
api.add_router('/comments', comments_router)


@user_router.post("/create_user")
def create_user(request, data: UserSchema):
    return UserService.create_user(data.user_name, data.password, data.role)


@user_router.put("/update_user", auth=JWTAuth())
def update_user(request, data: PartialUserSchema):
    user_name = request.auth['user_name']
    return UserService.update_user_by_user_name(user_name, data)


@user_router.post("/get_user_by_token", auth=JWTAuth())
def get_user_by_user_name(request):
    return UserService.get_user_by_user_name(request.auth['user_name'])


@user_router.delete("/delete_user/{user_id}", auth=JWTAuth())
def delete_user(request, user_id):
    user_id_req = request.auth['user_id']
    return UserService.delete_user(user_id, user_id_req)
