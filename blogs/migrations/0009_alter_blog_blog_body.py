# Generated by Django 5.0.6 on 2024-06-12 21:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0008_alter_blog_blog_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="blog_body",
            field=ckeditor.fields.RichTextField(max_length=2000),
        ),
    ]
