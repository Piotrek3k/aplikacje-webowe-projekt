# Generated by Django 4.1.5 on 2023-01-04 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookweb_app', '0007_alter_review_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
    ]
