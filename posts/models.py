from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

