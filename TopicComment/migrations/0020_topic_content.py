# Generated by Django 3.1.2 on 2020-10-06 16:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TopicComment', '0019_auto_20201006_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
