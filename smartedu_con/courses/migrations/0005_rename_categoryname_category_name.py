# Generated by Django 4.2.7 on 2023-11-18 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categoryName',
            new_name='name',
        ),
    ]
