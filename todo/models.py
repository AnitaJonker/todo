from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#users


#list
#status
#tag 
#text
#tsaks

class List(models.Model):
    list_name = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
#task
#task number
#task status
#list reference
#list
#tag 



class Task(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE,related_name='tasks')
    task_name= models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    
    #Tags
#tag name
#tag icon
    
class Tag(models.Model):
    lists = models.ForeignKey(List, on_delete=models.CASCADE)
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=20)
    tag_icon = models.CharField(max_length=20)
    


