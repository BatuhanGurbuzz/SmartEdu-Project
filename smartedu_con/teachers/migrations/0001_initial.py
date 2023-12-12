# Generated by Django 4.2.7 on 2023-11-21 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Teacher Name')),
                ('title', models.CharField(max_length=50, verbose_name='Teacher career')),
                ('description', models.TextField(blank=True, verbose_name='Teacher Description')),
                ('image', models.ImageField(upload_to='teachers/%Y/%m/%d/', verbose_name='Teacher Image')),
                ('facebook', models.URLField(blank=True, max_length=100, verbose_name='Teacher Facebook')),
                ('twitter', models.URLField(blank=True, max_length=100, verbose_name='Teacher Twitter')),
                ('linkedin', models.URLField(blank=True, max_length=100, verbose_name='Teacher Linkedin')),
                ('youtube', models.URLField(blank=True, max_length=100, verbose_name='Teacher Youtube')),
            ],
        ),
    ]