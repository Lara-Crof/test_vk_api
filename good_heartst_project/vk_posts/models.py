from django.db import models


class VkPostModel(models.Model):
    """Модель Поста из вконтакте."""
    text_vk = models.TextField(max_length=4096,
                               verbose_name='Текст_поста',
                               )
    photo_vk = models.URLField(max_length=4096,
                               verbose_name='Фото_поста'
                               )
