from django.shortcuts import get_object_or_404
from article.models import Article, Category
from article.schemas import ArticleResponseSchema
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
        return ArticleResponseSchema(
            id=article.id,
            title=article.title,
            content=article.content,
            author_id=article.author.id,
            category_id=article.category.id if article.category else None
        )

    def update_article(self, article_id, user_id, data):
        article = get_object_or_404(Article, id=article_id)

        if article.author.id != user_id:
            return None
        for field, value in data.dict(exclude_unset=True).items():
            setattr(article, field, value)
        article.save()

        return ArticleResponseSchema(
            id=article.id,
            title=article.title,
            content=article.content,
            author_id=article.author.id,
            category_id=article.category.id if article.category else None
        )

    def delete_article(self, article_id, user_id):
        article = get_object_or_404(Article, id=article_id)

        if article.author.id != user_id:
            return False

        article.delete()
        return True

    def get_article_by_id(self, article_id):
        article = get_object_or_404(Article, id=article_id)
        return ArticleResponseSchema(
            id=article.id,
            title=article.title,
            content=article.content,
            author_id=article.author.id,
            category_id=article.category.id if article.category else None
        )
