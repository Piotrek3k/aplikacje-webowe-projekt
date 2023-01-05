# Generated by Django 4.1.5 on 2023-01-04 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookweb_app', '0004_author_rename_name_book_title_book_createdat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='bookweb_app.author'),
            preserve_default=False,
        ),
    ]