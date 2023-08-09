from django.db import models

# Create your models here



class Teacher(models.Model):
    teacherId = models.IntegerField(primary_key = True)
    teacherFirstName = models.CharField(max_length = 20)
    teacherMiddleName = models.CharField ( max_length = 20 )
    teacherLastName = models.CharField ( max_length = 20 )
    teacherGender = models.CharField ( max_length = 6 )
    teacherEmail = models.EmailField ( )
    teacherPhoneNumber = models.CharField (max_length=  13 )
    teacherAddress = models.TextField ( max_length = 100 )
    teacherJoiningDate = models.DateTimeField ( )
    teacherRemarks = models.TextField ( max_length = 100 )
    teacherDescipline = models.CharField ( max_length = 10 )


class Students(models.Model):
    studentId = models.IntegerField(primary_key = True)
    studentFirstName = models.CharField(max_length = 20)
    studentMiddleName = models.CharField(max_length = 20)
    studentLastName= models.CharField(max_length = 20)
    studentGender = models.CharField ( max_length = 6 )
    studentEmail= models.EmailField()
    studentPhoneNumber = models.CharField(max_length= 13)
    studentAddress = models.TextField(max_length = 100)
    studentStandard = models.IntegerField()
    studentAdmissionDate= models.DateTimeField()
    studentRemarks = models.TextField(max_length = 100)
    studentDescipline = models.CharField(max_length = 10)

class StudentStandard(models.Model):
    standardId = models.IntegerField(primary_key = True)
    standardName = models.CharField(max_length= 20)
    standardBuildingName = models.CharField(max_length = 20)
    teacher = models.ManyToManyField(Teacher, related_name = 'standards')




















