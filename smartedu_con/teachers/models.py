from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name="Teacher Name")

    title = models.CharField(max_length=50, verbose_name="Teacher career")

    description = models.TextField(blank=True, verbose_name="Teacher Description")

    image = models.ImageField(upload_to="teachers/%Y/%m/%d/", verbose_name="Teacher Image")

    facebook = models.URLField(max_length=100, blank=True, verbose_name="Teacher Facebook")

    twitter = models.URLField(max_length=100, blank=True, verbose_name="Teacher Twitter")

    linkedin = models.URLField(max_length=100, blank=True, verbose_name="Teacher Linkedin")

    youtube = models.URLField(max_length=100, blank=True, verbose_name="Teacher Youtube")

    def __str__(self):
        return self.name
