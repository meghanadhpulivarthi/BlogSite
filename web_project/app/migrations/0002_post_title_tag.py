# Generated by Django 3.2.14 on 2022-07-05 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='BlogSite', max_length=255),
        ),
    ]
