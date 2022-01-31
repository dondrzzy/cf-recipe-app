from django.db import models

# Create your models here.

from ingredient.models import Ingredient


class Recipe(models.Model):

    name = models.CharField(max_length=120)
    ingredients = models.ManyToManyField(Ingredient, related_name="ingredients", blank=True, null=True)
    cooking_time = models.IntegerField(blank=True, null=True)
    description = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.name)
