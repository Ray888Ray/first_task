# Generated by Django 4.2.2 on 2023-06-18 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardGreeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('city', models.CharField(max_length=20, verbose_name='city')),
                ('username', models.CharField(max_length=20, verbose_name='username')),
            ],
        ),
    ]