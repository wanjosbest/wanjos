# Generated by Django 4.2 on 2024-11-20 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0025_passwordreset'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PasswordReset',
        ),
    ]
