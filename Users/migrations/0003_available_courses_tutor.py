# Generated by Django 4.2 on 2024-11-11 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_available_courses_liveclass_studentattendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='available_courses',
            name='tutor',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
