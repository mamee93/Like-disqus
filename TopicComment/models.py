from django.db import models
from django.contrib.auth.models import User
from  django.utils import timezone
# Create your models here.

class Topic(models.Model):
	user       = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE  )
	topc_title = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now=True) 
	update_at  = models.DateTimeField(auto_now_add=True)
	like      = models.ManyToManyField(User,blank=True)
	# comments   = models.ForeignKey('comments', related_name='Comments:', on_delete=models.CASCADE  )
	def __str__(self):
		return self.topc_title


class Comments(models.Model):
	userComment = models.ForeignKey(User, related_name='userComment', on_delete=models.CASCADE,blank=True,null=True  )
	topc_title  = models.ForeignKey('Topic', related_name='Comments_Topic', on_delete=models.CASCADE  )
	comments    = models.TextField(max_length=100)
	created_at  = models.DateTimeField(default=timezone.now)
	reply       = models.ForeignKey('self',related_name='replyies',null=True, on_delete=models.CASCADE)
	update_at   = models.DateTimeField(auto_now_add=True)
	# image      = models.ImageField(upload_to='CommintImg/')


	def __str__(self):
		return self.comments
	@property
	def num_like(self):
		return self.likes.all().count()
    # commients