from django.db import models


class Program(models.Model):
    id_user = models.IntegerField(verbose_name="id_user", default=None)
    name = models.CharField(max_length=20, verbose_name="Имя программы")
    program = models.TextField(verbose_name="Программа")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программы"


class Pictures(models.Model):
    title = models.CharField(max_length=20, verbose_name="Название")
    pictures = models.ImageField(upload_to="photos/", verbose_name="Картинка")

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"


