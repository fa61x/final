from django.db import models


# Create your models here.

class Department(models.Model):
    deptName = models.CharField(max_length=50)


class Course(models.Model):
    courseName = models.CharField(max_length=50)
    depatment = models.ForeignKey(Department, on_delete=models.CASCADE)


class Enquiry(models.Model):
    studentName = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    purpose_choices = [('enquiry', 'For Enquiry'), ('order', 'Place Order'), ('return', 'Return')]
    purpose = models.CharField(max_length=20, choices=purpose_choices)
    Materials = models.CharField(max_length=50)
    courseName = models.ForeignKey(Course, on_delete=models.CASCADE)
