from django.db import models
from django.core.validators import MaxLengthValidator, MinValueValidator, EmailValidator


class Parent(models.Model):
    name = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    age = models.IntegerField(validators=[MinValueValidator(18)])
    email = models.EmailField(validators=[EmailValidator()], default='no-reply@example.com')
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_info(self):
        return f'{self.name}, {self.age} years old'
