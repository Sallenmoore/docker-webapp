from django.test import TestCase
from api.models.course import Course

class AnimalTestCase(TestCase):
    def setUp(self):
        Course.objects.create(name="Introduction to Programming", semester="FALL")
        Course.objects.create(name="Introduction to English", semester="SPRING")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        cs = Course.objects.get(name="Introduction to Programming")
        english = Course.objects.get(name="Introduction to English")
        self.assertEqual(cs.semester, 'FALL')
        self.assertEqual(english.semester, 'SPRING')