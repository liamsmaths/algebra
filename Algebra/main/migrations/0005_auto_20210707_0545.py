# Generated by Django 3.2.4 on 2021-07-07 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_topic_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='video_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='studenttopic',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_topics', to='main.topic'),
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]