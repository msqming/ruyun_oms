# Generated by Django 2.1 on 2019-04-29 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='登录用户名')),
                ('pwd', models.CharField(max_length=64, verbose_name='登录密码')),
            ],
        ),
    ]