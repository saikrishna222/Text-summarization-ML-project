# Generated by Django 2.2.4 on 2021-05-17 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_documentuploadmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentuploadmodel',
            name='dno',
            field=models.IntegerField(default=True),
        ),
    ]