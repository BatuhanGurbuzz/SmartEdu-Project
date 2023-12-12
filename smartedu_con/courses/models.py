from django.db import models
from teachers.models import Teacher
from django.contrib.auth.models import User


# Category Start

class Category(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name="Category Name")

    slug = models.SlugField(max_length=50, unique=True, null=True, verbose_name="Category Link")

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    tagName = models.CharField(max_length=50, null=True, verbose_name="Tag Name")

    slug = models.SlugField(max_length=50, unique=True, null=True, verbose_name="Tag Link")

    def __str__(self):
        return self.tagName

# Category End


# Course Start
class Course(models.Model):
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=255, unique=True, verbose_name="Course Name")

    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)

    tags = models.ManyToManyField(Tag, blank=True, null=True)

    students = models.ManyToManyField(User, blank=True, related_name='courses_joined')

    description = models.TextField(blank=True, null=True, verbose_name="Course Description")
    
    image = models.ImageField(upload_to="courses/%Y/%m/%d/", default="courses/default.jpg", verbose_name="Course Image")
    
    date = models.DateTimeField(auto_now=True)
    
    avaliable = models.BooleanField(default=True, verbose_name="Course Avaliable")

    def __str__(self):
        return self.name

# Course End