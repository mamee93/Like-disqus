# Generated by Django 3.1.2 on 2020-10-07 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TopicComment', '0021_remove_comments_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='TopicComment.comments'),
        ),
    ]
