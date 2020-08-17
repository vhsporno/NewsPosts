from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.ManyToOneRel(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    upvotes_amount = models.IntegerField(default=0)

    def getAuthor(self):
        return getattr(self.author, 'id')