# Generated by Django 3.2.9 on 2021-12-05 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=26)),
                ('name', models.CharField(max_length=26)),
                ('Date_Of_Birth', models.DateTimeField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Select Gender', max_length=25)),
                ('role', models.CharField(choices=[('Staff', 'Staff'), ('Teacher', 'Teacher'), ('Student', 'Student')], default='Role', max_length=25)),
            ],
        ),
    ]
