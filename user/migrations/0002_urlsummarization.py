# Generated by Django 2.2.4 on 2021-05-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlSummarization',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('user_mail', models.EmailField(max_length=254)),
                ('summarized_content', models.TextField()),
                ('content_keywords', models.TextField()),
                ('len_total_content', models.CharField(max_length=100)),
                ('len_summarized_content', models.CharField(max_length=100)),
            ],
        ),
    ]
