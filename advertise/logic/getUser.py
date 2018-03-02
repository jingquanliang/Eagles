__author__ = 'jql'

from django.test import TestCase
from advertise.models import Person


class AnimalTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name="lion", age=30)
        Person.objects.create(name="cat", age=20)

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Person.objects.get(name="lion")
        cat = Person.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')

if __name__ == '__main__':
    testA=AnimalTestCase()
    testA.setUp()
    testA.test_animals_can_speak()
