# Generated by Django 3.1.5 on 2021-01-18 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_title',
            new_name='title',
        ),
    ]
