from pyexpat import model
from statistics import mode
from django.db import models


class FindHome(models.Model):
    ANIMAL_CHOICES = (
        ('CAT', 'Котик'),
        ('DOG', 'Собачка')
    )
    GENDER_CHOICES = (
        ('M', 'Мальчик'),
        ('F', 'Девочка'),
    )
    HEALTH_CHOICES = (
        ('1', 'Полностью здоров'),
        ('2', 'Нуждаеться в легком лечение'),
        ('3', 'Нуждается в лечение'),
        ('4', 'Требуеться операция'),
        ('5', 'Мы с Вами вылечили его благодарая Вашей помощи'),
    )

    TYPE_CHOICES = (
        ('shelter', 'Ищит дом'),
        ('funds_for_treatment', 'Временная передержка'),
        ('temporary_overexposure', 'Требуеться лечение')
    )
    gender = models.CharField(
        max_length=1,
        default='M', 
        choices=GENDER_CHOICES
        )
    
    type_animal = models.CharField(
        max_length=3,
        choices=ANIMAL_CHOICES, 
        verbose_name='Тип животного', default='CAT'
     )
    
    #locations = models.
    locations_comment = models.TextField(
        blank=True, 
        verbose_name='Короткое описание места'
    )
    age = models.CharField(
        max_length=25, 
        verbose_name='примерный возрасту '
    )
    help_an = models.CharField(
        max_length=40,
        choices=TYPE_CHOICES,
        verbose_name='Тип помощи',
        default='shelter'
    )
    
    description =models.TextField(
        verbose_name=('История животного'),
        help_text='Расскажите о крохе'
        )
    health = models.CharField(
        max_length=40, 
        choices=HEALTH_CHOICES,
        default='1')

    photo = models.ImageField(
        upload_to ='animals/%Y/%m/%d/', 
        null=True, 
        blank=True, 
        verbose_name='Фото животных которым нужен дом')
    creat_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
        )
    update_up = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    is_publish = models.BooleanField(
        default=True,
        verbose_name='Опубликовать'
    )
    actualish = models.BooleanField(
        default=True, 
        verbose_name='Акнтуальность'
        )
   

    #def get_absolute_url(self):
        #"""Method for a category that specifies a specific category"""
        #return reverse("category", kwargs={"category_id": self.pk})

    def __str__(self):
        return self.update_up
    
    verbose_name = 'Животное'
    verbose_name_plural = 'Животные'
    ordering = ['-creat_at']



# class Animals(models.Model):
#     """Dog or cats"""
#     ANIMAL_CHOICES = (
#         ('CAT', 'Котик'),
#         ('DOG', 'Собачка')
# )
#     type_animal = models.CharField(
#         max_length=3,
#         choices=ANIMAL_CHOICES, 
#         verbose_name='Тип животного', default='CAT'
#      )
    
  


class Helps_of_animals(models.Model):
    TYPE_CHOICES = (
        ('shelter', 'Ищит дом'),
        ('funds_for_treatment', 'Временная передержка'),
        ('temporary_overexposure', 'Требуеться лечение')
    )
    title = models.CharField(
        max_length=40, 
        choices=TYPE_CHOICES,
        verbose_name='Тип помощи'
    )
    time_assistance = models.CharField(
         max_length=240
    )
    class Meta:
        verbose_name = 'Тип помощи'
        verbose_name_plural = 'Тип помощи'
        ordering = ['-time_assistance']
        
# class Health_level(models.Model):
#     HEALTH_CHOICES = (
#         ('1', 'Полностью здоров'),
#         ('2', 'Нуждаеться в легком лечение'),
#         ('3', 'Нуждается в лечение'),
#         ('4', 'Требуеться операция'),
#         ('5', 'Мы с Вами вылечили его благодарая Вашей помощи'),
#     )
#     health = models.CharField(max_length=40, choices=HEALTH_CHOICES,
#                               default='1')






