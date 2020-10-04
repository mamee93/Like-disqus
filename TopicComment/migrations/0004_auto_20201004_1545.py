# Generated by Django 3.1.2 on 2020-10-04 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TopicComment', '0003_remove_topic_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='userComment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userComment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comments',
            name='topc_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comments_Topic', to='TopicComment.topic'),
        ),
    ]
