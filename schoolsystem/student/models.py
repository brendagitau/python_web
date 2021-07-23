import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


from django.db import models

# Create your models here.



def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

NATIONALITY=(
    ("KENYAN","KENYAN"),
    ("UGANDAN","UGANDAN"),
    ("RWANDESE","RWANDESE"),
    ("SOUTH SUDANESE","SOUTH SUDANESE"),
)
GENDER=(
    ("MALE","MALE"),
    ("FEMALE","FEMALE"),
    ("NON-BINARY","NON-BINARY"),
    ("TRANSGENDER","TRANSGENDER"),

)

class Student(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    birth_date =models.DateField()
    nationality = models.CharField(max_length=20, choices = NATIONALITY,
        default = 'KENYAN')
    gender = models.CharField(max_length=20, choices = GENDER,
        default = 'FEMALE')
    student_id = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    admission_date =models.DateField()
    guardian_name = models.CharField(max_length=30)
    guardian_phone_number = models.CharField(max_length=20)
    medical_report=models.FileField(upload_to='documents/%Y/%m/%d')
    room_number = models.PositiveSmallIntegerField()
    class_name =models.CharField(max_length=20)
    academic_year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1984),max_value_current_year])
    email =models.EmailField()
    city =models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')

    


     