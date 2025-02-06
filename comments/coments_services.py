from django.shortcuts import get_object_or_404
from article.models import Article
from comments.models import Comment
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
        return comment

    def update_comment(self, comment_id, user_id, content):
        comment = get_object_or_404(Comment, id=comment_id)

        if comment.author.id != user_id:
            return None

        comment.content = content
        comment.save()
        return comment

    def delete_comment(self, comment_id, user_id):
        comment = get_object_or_404(Comment, id=comment_id)

        if comment.author.id != user_id:
            return False

        comment.delete()
        return True

    def get_comments_by_article(self, article_id):
        return Comment.objects.filter(article_id=article_id)
