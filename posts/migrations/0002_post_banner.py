# Generated by Django 5.1.4 on 2024-12-25 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(default='nonImage.png', upload_to=''),
        ),
    ]
