# Generated by Django 5.0.6 on 2024-06-08 16:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0003_alter_blog_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blog",
            old_name="short_desription",
            new_name="short_description",
        ),
    ]