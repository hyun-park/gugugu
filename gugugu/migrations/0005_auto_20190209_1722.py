# Generated by Django 2.1.5 on 2019-02-09 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gugugu', '0004_auto_20190208_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(max_length=1024),
        ),
    ]