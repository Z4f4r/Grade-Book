from django.db import models


class Course(models.Model):
    title = models.CharField('Имя', max_length=255)
    description = models.TextField('О курсе')
    start_time = models.DateTimeField('Начало курса',
                                      blank=True,
                                      null=True)
    end_time = models.DateTimeField('Последний урок',
                                    blank=True,
                                    null=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self) -> models.CharField:
        return self.title
