# Generated by Django 4.2.4 on 2024-01-10 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_tags_delete_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment',
        ),
    ]
