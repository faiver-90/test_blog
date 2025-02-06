from django.shortcuts import get_object_or_404
from article.models import Article
from comments.models import Comment
from comments.schemas import CommentResponseSchema
from users.models import User


class CommentService:
    def create_comment(self, user_id, article_id, content):
        user = get_object_or_404(User, id=user_id)
        article = get_object_or_404(Article, id=article_id)

        comment = Comment.objects.create(
            author=user,
            article=article,
            content=content
        )
        return CommentResponseSchema(
            id=comment.id,
            content=comment.content,
            author_id=comment.author.id,
            article_id=comment.article.id
        )

    def update_comment(self, comment_id, user_id, content):
        comment = get_object_or_404(Comment, id=comment_id)

        if comment.author.id != user_id:
            return None

        comment.content = content
        comment.save()
        return CommentResponseSchema(
            id=comment.id,
            content=comment.content,
            author_id=comment.author.id,
            article_id=comment.article.id
        )

    def delete_comment(self, comment_id, user_id):
        comment = get_object_or_404(Comment, id=comment_id)

        if comment.author.id != user_id:
            return False

        comment.delete()
        return True

    def get_comments_by_article(self, article_id):
        comments = Comment.objects.filter(article_id=article_id)
        return [CommentResponseSchema(
            id=comment.id,
            content=comment.content,
            author_id=comment.author.id,
            article_id=comment.article.id
        ) for comment in comments]
