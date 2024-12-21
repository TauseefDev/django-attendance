from django.db import models
from django.utils.timezone import now

# Create your models here.

class Student(models.Model):

    MATHS_PREF = [
        ('Maths', 'Maths' ),
        ('Non-Maths', 'Non-Maths' )
    ]

    name = models.CharField(max_length=100)
    roll_number = models.PositiveIntegerField()
    maths = models.CharField(max_length=15,choices=MATHS_PREF)
    email = models.EmailField()
    phone = models.CharField(max_length=15)


    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('Present', 'Present'),
                                                       ('Absent', 'Absent'),
                                                       ('Non-maths', 'Non-maths'),
                                                         ('Halfday', 'Halfday')],default='Present'
                                                         )

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"
    


