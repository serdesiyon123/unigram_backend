# Generated by Django 4.2.11 on 2024-04-03 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile'),
        ('post', '0008_rename_comment_comment_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='saves',
        ),
        migrations.AddField(
            model_name='comment',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
    ]