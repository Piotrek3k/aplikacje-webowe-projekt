# Generated by Django 4.1.5 on 2023-01-03 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookweb_app', '0002_rename_movie_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='description',
            new_name='desc',
        ),
    ]
