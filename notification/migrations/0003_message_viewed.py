# Generated by Django 3.1 on 2020-09-03 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_remove_message_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
    ]