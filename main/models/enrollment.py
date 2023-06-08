# from django.db import models
#
#
# class Enrollment(models.Model):
#     student = models.ForeignKey('main.student', on_delete=models.CASCADE)
#     course = models.ForeignKey('main.course', on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name = 'Регистрация'
#         verbose_name_plural = 'Регистрация'
#
#     def __str__(self) -> str:
#         return f'{self.student.name}-{self.course.title}'
