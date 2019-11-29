from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=100)
    # Avoid multiple emails,
    # so the unique set to True
    email = models.EmailField(max_length=100, unique=True)
    # enable the message could be empty,set the blank = True
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
