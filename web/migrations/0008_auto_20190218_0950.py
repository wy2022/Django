# Generated by Django 2.1.7 on 2019-02-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20190216_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='uptime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]