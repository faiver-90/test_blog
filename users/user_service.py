from django.forms import model_to_dict
from django.shortcuts import get_object_or_404

from users.models import User


class UserService:
    @staticmethod
    def create_user(user_name, password):
        user = User.objects.create(user_name=user_name, password=password)
        user.save()
        return {'detail': "User created"}

    @staticmethod
    def update_user_by_user_name(user_name, data):
        user = get_object_or_404(User, user_name=user_name)

        for field, value in data.dict(exclude_unset=True).items():
            setattr(user, field, value)
        user.save()
        return {'detail': "User update"}

    @staticmethod
    def get_user_by_user_name(user_name):
        user = get_object_or_404(User, user_name=user_name)
        return model_to_dict(user)

    def delete_user(self, user_id):
        pass
