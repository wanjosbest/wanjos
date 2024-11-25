# Generated by Django 4.2 on 2024-11-21 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0032_remove_studentatten_student_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='examtimetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, unique=True)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('link', models.CharField(max_length=255, null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timetableexam', to='Users.coursemodule')),
            ],
        ),
    ]