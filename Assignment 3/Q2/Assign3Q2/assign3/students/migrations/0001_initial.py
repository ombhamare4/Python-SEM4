# Generated by Django 3.2 on 2021-05-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('current_sem', models.IntegerField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('cgpi', models.IntegerField(max_length=50)),
            ],
        ),
    ]
