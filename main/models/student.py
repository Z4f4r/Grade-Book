from django.core.validators import RegexValidator
from django.db import models


class Student(models.Model):
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    email = models.EmailField('Почта')
    create_time = models.DateTimeField("Дата создания",
                                       auto_now_add=True)
    update_time = models.DateTimeField("Дата обновления",
                                       auto_now=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,12}$',
        message="Номер телефона должен быть в формате: '+999999999999'. Максимальное количество цифр: 12."
    )
    phone = models.CharField('Телефон', validators=[phone_regex], max_length=12)
    photo = models.ImageField("Фото", upload_to='photos/%y/%m/%d',
                              blank=True,
                              null=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
