# Generated by Django 2.2.4 on 2021-05-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_documentsummarizationmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentsummarizationmodel',
            name='dno',
            field=models.IntegerField(default=True),
        ),
    ]