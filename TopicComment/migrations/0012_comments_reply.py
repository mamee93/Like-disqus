# Generated by Django 3.1.2 on 2020-10-05 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TopicComment', '0011_auto_20201005_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replyies', to='TopicComment.comments'),
        ),
    ]
