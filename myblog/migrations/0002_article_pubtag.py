# Generated by Django 2.1.7 on 2019-03-20 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pubTag',
            field=models.BooleanField(default=False),
        ),
    ]