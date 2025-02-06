from django.shortcuts import get_object_or_404
from article.models import Article, Category
from users.models import User


class ArticleService:
    def create_article(self, user_id, data):
        user = get_object_or_404(User, id=user_id)
        category = get_object_or_404(Category, id=data.category_id)

        article = Article.objects.create(
            title=data.title,
            content=data.content,
            author=user,
            category=category
        )
        return article

    def update_article(self, article_id, user_id, data):
        article = get_object_or_404(Article, id=article_id)

        if article.author.id != user_id and not self.is_admin(user_id):
            return None

        article.title = data.title
        article.content = data.content
        article.save()
        return article

    def delete_article(self, article_id, user_id):
        article = get_object_or_404(Article, id=article_id)

        if article.author.id != user_id and not self.is_admin(user_id):
            return False

        article.delete()
        return True

    def get_article_by_id(self, article_id):
        return get_object_or_404(Article, id=article_id)

    def is_admin(self, user_id):
        user = get_object_or_404(User, id=user_id)
        return user.role == "admin"
