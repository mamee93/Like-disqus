# Generated by Django 3.1.2 on 2020-10-05 09:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TopicComment', '0005_remove_comments_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='likes',
            field=models.ManyToManyField(related_name='like_topic', to=settings.AUTH_USER_MODEL),
        ),
    ]
