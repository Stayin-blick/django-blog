# Generated by Django 4.2.16 on 2024-11-26 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_post_feature_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="feature_image",
            new_name="featured_image",
        ),
    ]
