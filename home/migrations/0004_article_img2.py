# Generated by Django 4.1.7 on 2023-03-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_article_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img2',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]