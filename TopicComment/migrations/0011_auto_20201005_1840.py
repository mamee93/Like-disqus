# Generated by Django 3.1.2 on 2020-10-05 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TopicComment', '0010_auto_20201005_1819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='likes',
            new_name='like',
        ),
    ]
