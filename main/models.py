from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import datetime
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='url')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='url')
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    date_event = models.DateTimeField(verbose_name='Дата события', default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликованно')
    image = models.ImageField(upload_to='image/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='post', verbose_name='категория')

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']


class Team(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='e-mail')
    resume = models.TextField(blank=True, verbose_name='Опыт работы')
    photo = models.ImageField(max_length=200, verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')

    def get_absolut_url(self):
        return reverse('team', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команда'
        ordering = ['created_at']


class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=254, unique=True, verbose_name='e-mail')
    message = models.TextField(blank=False, verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Отправленно')

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return self.name


class Subscriptions(models.Model):
    GROUP = (
        ('1', 'от 2 до 4 лет'),
        ('2', 'от 5 до 10 лет'),
        ('3', 'Ленинградское ш., 27, Дмитровское ш., 79'),
        ('4', 'Индивидуальная тренировка'),
    )
    CONNECT = (
        ('P', 'Телефонный звонок'),
        ('T', 'Telegram'),
        ('W', 'WhatsApp'),
    )
    name_group = models.CharField(max_length=100, verbose_name='Группа', choices=GROUP, default='1')
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = PhoneNumberField(unique=True, null=False, blank=False, verbose_name='Телефон')
    connection = models.CharField(max_length=100, verbose_name='Связаться по', choices=CONNECT, default='P')

    class Meta:
        verbose_name = 'Заявка на абонимент'
        verbose_name_plural = 'Заявка на абонимент'
