# Generated by Django 4.2.11 on 2024-03-31 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_alter_post_downvote_alter_post_likes_alter_post_tags_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=600),
        ),
    ]
