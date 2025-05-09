from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

#Question
class Question(models.Model):
   user  = models.ForeignKey(User, on_delete=models.CASCADE)
   title = models.CharField(max_length=200)
   detail = models.TextField()
   add_time = models.DateTimeField(auto_now_add=True)

   def __str__(self):
        return self.title
    
# Answer    
class Answer(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_user')
   question = models.ForeignKey(Question, on_delete=models.CASCADE)
   detail = models.TextField()
   add_time = models.DateTimeField(auto_now_add=True)

   def __str__(self):
        return self.detail    
    
    
# Comment

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user') 
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    comments = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    
    
# Upvote

class Upvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upvote_user')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
      
# Downvote
class Downvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='downvote_user')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)       