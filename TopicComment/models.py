from django.db import models
from django.contrib.auth.models import User
from  django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.

class Topic(models.Model):
	user       = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE  )
	topc_title = models.CharField(max_length=100)
	content    = RichTextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now=True) 
	update_at  = models.DateTimeField(auto_now_add=True)
	like      = models.ManyToManyField(User,default=None,blank=True,)
	image = models.ImageField(upload_to='imageTopic/',null=True)
	 
	def __str__(self):
		return self.topc_title


class Comments(models.Model):
	userComment = models.ForeignKey(User, related_name='userComment', on_delete=models.CASCADE,blank=True,null=True  )
	topc_title  = models.ForeignKey('Topic', related_name='Comments_Topic', on_delete=models.CASCADE  )
	comments    = RichTextField(blank=True, null=True)
	created_at  = models.DateTimeField(default=timezone.now)
	reply      = models.ForeignKey('self',related_name='replies',on_delete=models.CASCADE,null=True )
	update_at   = models.DateTimeField(auto_now_add=True)
	 
	class Meta:
		ordering = ['-update_at']


	def __str__(self):
		return self.comments
	@property
	def num_like(self):
		return self.likes.all().count()

 

class Like(models.Model):
	LIKE_CHOICES = (
	('Like','Like'),
	('UnLike','UnLike')
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
	topic = models.ForeignKey(Topic,related_name='topic_like', on_delete=models.CASCADE,blank=True,null=True)
	value = models.CharField(max_length=10,default='Like',choices=LIKE_CHOICES)
		
