from django.db import models


class Artslice(models.Model):
    id = models.AutoField('id', primary_key=True)
    full_name = models.CharField('ФИО', max_length=50)
    email = models.CharField('Почта', max_length=50)
    group = models.CharField('Группа', max_length=50)
    sort = models.CharField(max_length=50, default='-group', editable=False)

    def __str__(self):
        return f'{self.full_name}'

    def get_absolute_url(self):
        return f'/update/{self.id}'

    class Meta:
        verbose_name = 'База данных студентов'
        verbose_name_plural = 'База данных студентов'

