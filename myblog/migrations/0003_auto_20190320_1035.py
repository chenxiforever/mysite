# Generated by Django 2.1.7 on 2019-03-20 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_article_pubtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(default=False, upload_to=''),
        ),
    ]