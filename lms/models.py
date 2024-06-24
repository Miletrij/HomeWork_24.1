from django.db import models

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    image = models.ImageField(upload_to='course', verbose_name='картинка', **NULLABLE)
    content = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    image = models.ImageField(upload_to='lesson', verbose_name='картинка', **NULLABLE)
    content = models.TextField(verbose_name='описание', **NULLABLE)
    url = models.URLField(verbose_name='видео по ссылке', **NULLABLE)
    course = models.ForeignKey(Course, verbose_name='курсы', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
