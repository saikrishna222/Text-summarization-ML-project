# Generated by Django 2.2.4 on 2021-05-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_urlsummarization'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlsummarization',
            name='url_link',
            field=models.TextField(default=True),
        ),
    ]
