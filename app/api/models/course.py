from django.db import models

class Course(models.Model):
    SEMESTERS = [
        ("FALL", "Fall"),
        ("SPRING", "Spring"),
        ("SUMMER", "Summer"),
    ]
    name = models.CharField(max_length=30)
    semester = models.CharField(max_length=255, choices=SEMESTERS)