from django.db import models
from  django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text  import slugify
from django.db.models.signals import post_save
# Create your models here.

class  Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/')
    phon_number = models.CharField(max_length=15)
    slug = models.SlugField(blank=True,null=True)
    bio = models.TextField(blank=True)
    haedline = models.CharField(max_length=15,blank=True)
    created_at = models.DateTimeField(auto_now=True) 
    

    def __str__(self):
        return '%s' %(self.user)

    def save(self, *args, **kwargs):
    	if not self.slug:
    		self.slug = slugify(self.user)
    	super(Profile, self).save(*args,**kwargs)

    @property
    def image_url(self):
    	if self.image and hasattr(self.image, 'url'):
    		return self.image.url

@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_user_profile,sender=User)