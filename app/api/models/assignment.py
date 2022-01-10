from django.db import models
from datetime import datetime
import copy


class Assignment(models.Model):
    ATYPE = [
        ("EXAM", "Exam"),
        ("PROJECT", "Project"),
        ("LAB", "Lab"),
        ("REVIEW", "Review"),
        ("EXERCISE", "Exercise"),
    ]
    LANGUAGES =  [('py', 'Python'), ('c', 'C'), ('js', 'Javascript'), ('cpp', 'C++')]
    type = models.CharField(max_length=255, choices=ATYPE)
    is_vc = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    description_url = models.URLField()
    max_points = models.IntegerField()
    gradebook_name = models.CharField(max_length=255)
    _due_date = models.DateTimeField(null=True, blank=True)
    available_date = models.DateTimeField(null=True, blank=True)
    submissions_last_updated = models.DateTimeField(null=True, blank=True)
    fork_url = models.URLField(null=True, blank=True)
    repo_prefix = models.CharField(max_length=255, null=True, blank=True)
    template_repo_url = models.URLField(null=True, blank=True)
    language = models.CharField(default="py", max_length=80, choices=LANGUAGES)
    level = models.IntegerField(default=4, choices=[(1, 'Beginner'), (2, 'Basic'), (3, 'Proficient'), (4, 'Expert')])

    def __str__(self):
        return f"{self.chapter} {self.type} : {self.name}-{self.chapter.course}"

    @property
    def is_available(self):
        return datetime.now() > self.available_date if self.available_date else True

    @property
    def is_due(self):
        return datetime.now() > self.due_date if self.due_date else False

    def due_date(self):
        if self._due_date:
            return self._due_date
        else:
            return self.chapter.due_date

    def getGraderURL(self):
        url = f'{self.chapter.course.version_control_url}/{self.grader.get().grader_repo}'
        return url

    def serialize(self):
        serialized = {
            "pk": self.pk,
            "organization": f"{self.chapter.course.organization}/",
            "type": self.type,
            "grader-repo": self.grader.get().grader_repo,
            "points": self.max_points,
            "driver": self.grader.get().driver,
            "run": self.grader.get().run,
            "repo-prefix": self.repo_prefix,
            "sections": [s.pk for s in self.chapter.course.sections],
            "styles": [],
            "criteria": [],
            "inspect": [],
        }
        serialized["due-date"] = f"{self.due_date}"
        serialized['criteria'] = [{'msg': r.criteria, 'points': r.max_points, 'note': r.note, 'scale': r.scale}
                                 for r in self.grader.criteria.all()]

        serialized['styles'] = []
        return serialized

    def getGrader(self):
        from django.apps import apps
        Grader = apps.get_model('api', 'Grader')
        try:
            grader = self.grader.get()
        except Grader.DoesNotExist as e:
            kwargs = {"assignment": self, "run": "python main.py", "driver": "main.py"}
            grader = Grader(**kwargs)
            grader.save()

        return grader
