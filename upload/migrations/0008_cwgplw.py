# Generated by Django 2.1 on 2019-04-20 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0007_cwbjbxlw'),
    ]

    operations = [
        migrations.CreateModel(
            name='CwGplW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shijian', models.CharField(max_length=32, verbose_name='年月周')),
                ('pinlei', models.CharField(max_length=32, verbose_name='品类')),
                ('mbxse', models.BigIntegerField(verbose_name='月度目标销售额')),
                ('mbxl', models.IntegerField(verbose_name='月度目标销量')),
            ],
        ),
    ]