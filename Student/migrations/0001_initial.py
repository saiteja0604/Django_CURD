# Generated by Django 3.2.5 on 2021-07-27 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('StudentId', models.AutoField(primary_key=True, serialize=False)),
                ('StudentName', models.CharField(max_length=50)),
                ('StudentPhno', models.CharField(max_length=10)),
                ('StudentEmail', models.CharField(max_length=50)),
            ],
        ),
    ]
