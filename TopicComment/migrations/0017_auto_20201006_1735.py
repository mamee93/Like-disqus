# Generated by Django 3.1.2 on 2020-10-06 13:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TopicComment', '0016_auto_20201006_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
