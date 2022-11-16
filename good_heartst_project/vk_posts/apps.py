from django.apps import AppConfig

from .servise import start_parsing


class VkPostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vk_posts'

    # def ready(self):
    #     print('Запуск скрипта!')
    #     start_parsing()
