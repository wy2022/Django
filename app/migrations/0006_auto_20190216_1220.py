# Generated by Django 2.1.7 on 2019-02-16 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190216_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='insert_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(null=True),
        ),
    ]