# Generated by Django 3.1.2 on 2020-10-06 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TopicComment', '0018_comments_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-update_at']},
        ),
    ]
