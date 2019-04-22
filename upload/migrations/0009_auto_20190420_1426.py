# Generated by Django 2.1 on 2019-04-20 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0008_cwgplw'),
    ]

    operations = [
        migrations.CreateModel(
            name='CwGplM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shijian', models.CharField(max_length=32, verbose_name='年月周')),
                ('pinlei', models.CharField(max_length=32, verbose_name='品类')),
                ('mbxse', models.BigIntegerField(verbose_name='月度目标销售额')),
                ('mbxl', models.IntegerField(verbose_name='月度目标销量')),
            ],
        ),
        migrations.AddField(
            model_name='cwgplw',
            name='huod',
            field=models.CharField(default=0, max_length=128, verbose_name='运营活动'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cwgplw',
            name='mbxl',
            field=models.IntegerField(verbose_name='周度目标销量'),
        ),
        migrations.AlterField(
            model_name='cwgplw',
            name='mbxse',
            field=models.BigIntegerField(verbose_name='周度目标销售额'),
        ),
    ]
