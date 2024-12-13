from django.db import models

# Create your models here.
class BurgerMenu(models.Model):
    image = models.ImageField(upload_to='image/')
    title = models.CharField(max_length=60,verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Бургер'
        verbose_name_plural = 'Бургеры'
class BurgerBigMenu(models.Model):
    image = models.ImageField(upload_to='image/')
    title = models.CharField(max_length=60,verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class SocialMedia(models.Model):
    facebook = models.URLField(
        max_length=255,
        blank=True, 
        null=True, 
        verbose_name="Ссылка на Facebook"
        )
    instagram = models.URLField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name="Ссылка на Instagram"
                                )
    twitter = models.URLField(
        max_length=255,
        blank=True, 
        null=True, 
        verbose_name="Ссылка на Twitter"
        )
    google_plus = models.URLField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name="Ссылка на Google+"
        )

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    def __str__(self):
        return f"Ссылки на соцсети"

class BurgerMenuDetail(models.Model):
    image = models.ImageField(upload_to='image/')
    title = models.CharField(max_length=60,verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бургер детали'
        verbose_name_plural = 'Бургеры детали'