from django.db import models


class Pet(models.Model):
    MAX_NAME_LEN = 30
    name = models.CharField(
        max_length=MAX_NAME_LEN,
    )


class Person(models.Model):
    MAX_NAME_LEN = 30
    name = models.CharField(
        max_length=MAX_NAME_LEN,
    )
    age = models.PositiveIntegerField(),
    pets = models.ManyToManyField(
        Pet,
    )
