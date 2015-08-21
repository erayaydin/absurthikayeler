from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey("self", null=True, blank=True, related_name="contents")
    content = models.TextField()
    author = models.ForeignKey(User)
    type = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name="books")
    views = models.BigIntegerField(default=0)

    def __str__(self):
        return self.title

    def comments(self):
        return self.contents.filter(type=False)

    def newbooks(self):
        return self.contents.filter(type=True)

    def totalNewBooks(self):
        total = self.contents.filter(type=True).count()
        for comment in self.contents.filter(type=False):
            total += comment.contents.filter(type=True).count()

        return total