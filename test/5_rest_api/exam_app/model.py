from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20)
    address = models.TextField()

class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classrooms')
    year = models.CharField(max_length=10)
    label = models.CharField(max_length=20)

class Teacher(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers')

class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')
