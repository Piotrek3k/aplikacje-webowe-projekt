# Generated by Django 4.1.5 on 2023-01-12 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookweb_app', '0008_book_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]