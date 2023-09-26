from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField('Заголовок',max_length=50)              # Строка с огр знаками
    desc = models.TextField('Описание')              # Строка с огр знаками
    image = models.ImageField('Изображение',upload_to='blog/image/')   # Строка под изоброжение
    date = models.DateField('Дата')                            # Дата
    url = models.URLField('Доп.источник', blank=False)                              # Ссылка

    def __str__(self):
        return f"{self.title} | {self.date}"