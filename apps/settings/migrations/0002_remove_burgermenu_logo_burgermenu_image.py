# Generated by Django 5.1.3 on 2024-12-03 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='burgermenu',
            name='logo',
        ),
        migrations.AddField(
            model_name='burgermenu',
            name='image',
            field=models.ImageField(default=1, upload_to='image/'),
            preserve_default=False,
        ),
    ]
