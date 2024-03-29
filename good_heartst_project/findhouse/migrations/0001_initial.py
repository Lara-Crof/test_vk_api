# Generated by Django 3.2.15 on 2022-08-23 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FindHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Мальчик'), ('F', 'Девочка')], default='M', max_length=1)),
                ('type_animal', models.CharField(choices=[('CAT', 'Котик'), ('DOG', 'Собачка')], default='CAT', max_length=3, verbose_name='Тип животного')),
                ('locations_comment', models.TextField(blank=True, verbose_name='Короткое описание места')),
                ('age', models.CharField(max_length=25, verbose_name='примерный возрасту ')),
                ('help_an', models.CharField(choices=[('shelter', 'Ищит дом'), ('funds_for_treatment', 'Временная передержка'), ('temporary_overexposure', 'Требуеться лечение')], default='shelter', max_length=40, verbose_name='Тип помощи')),
                ('description', models.TextField(help_text='Расскажите о крохе', verbose_name='История животного')),
                ('health', models.CharField(choices=[('1', 'Полностью здоров'), ('2', 'Нуждаеться в легком лечение'), ('3', 'Нуждается в лечение'), ('4', 'Требуеться операция'), ('5', 'Мы с Вами вылечили его благодарая Вашей помощи')], default='1', max_length=40)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='animals/%Y/%m/%d/', verbose_name='Фото животных которым нужен дом')),
                ('creat_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('update_up', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_publish', models.BooleanField(default=True, verbose_name='Опубликовать')),
                ('actualish', models.BooleanField(default=True, verbose_name='Акнтуальность')),
            ],
        ),
        migrations.CreateModel(
            name='Helps_of_animals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('shelter', 'Ищит дом'), ('funds_for_treatment', 'Временная передержка'), ('temporary_overexposure', 'Требуеться лечение')], max_length=40, verbose_name='Тип помощи')),
                ('time_assistance', models.CharField(max_length=240)),
            ],
            options={
                'verbose_name': 'Тип помощи',
                'verbose_name_plural': 'Тип помощи',
                'ordering': ['-time_assistance'],
            },
        ),
    ]
