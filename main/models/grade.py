from django.core.validators import MaxValueValidator
from django.db import models


class Grade(models.Model):
    value = models.IntegerField('Балл', validators=[MaxValueValidator(10)])
    date = models.DateField('Дата')
    course = models.ForeignKey('main.course',
                               on_delete=models.CASCADE,
                               verbose_name='Курс')
    student = models.ForeignKey('main.student',
                                on_delete=models.CASCADE,
                                verbose_name='Студент')

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"

    def __str__(self) -> str:
        return f'{self.value}'
