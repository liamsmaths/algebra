# Generated by Django 3.2.4 on 2021-07-07 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210707_0545'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenttopic',
            name='correct_answer',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
