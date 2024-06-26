# Generated by Django 4.2.11 on 2024-04-04 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_profile_user'),
        ('post', '0016_alter_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='downvote',
            field=models.ManyToManyField(blank=True, related_name='downvoted_comment', to='user.profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='upvote',
            field=models.ManyToManyField(blank=True, related_name='upvoted_comment', to='user.profile'),
        ),
    ]
