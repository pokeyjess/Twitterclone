# Generated by Django 3.1 on 2020-09-05 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0003_myuser_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='About Me'),
        ),
    ]
