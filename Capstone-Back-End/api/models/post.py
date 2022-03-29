from django.db import models
from django.contrib.auth import get_user_model
from sqlite3 import Date
class Post(models.Model):
  title = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  content = models.CharField(max_length=500)
  created_at = Date.today()
  author = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )
  
  def __str__(self):
    # This must return a string
    return f"blogging is just the best {self.title}"   