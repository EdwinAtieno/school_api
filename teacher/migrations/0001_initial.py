# Generated by Django 3.2.9 on 2021-12-05 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tid', models.CharField(max_length=26)),
                ('user_id', models.TextField()),
                ('D_O_E', models.DateTimeField()),
                ('Department', models.CharField(choices=[('Languages', 'Languages'), ('Maths', 'Maths'), ('Sciences', 'Sciences'), ('Humanities', 'Humanities'), ('Others', 'Others'), ('Hr', 'Hr')], default='Departments', max_length=50)),
            ],
        ),
    ]