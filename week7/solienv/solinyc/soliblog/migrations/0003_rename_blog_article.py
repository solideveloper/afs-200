# Generated by Django 3.2.7 on 2022-01-31 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soliblog', '0002_rename_article_blog'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='Article',
        ),
    ]