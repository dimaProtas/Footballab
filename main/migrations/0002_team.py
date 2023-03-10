# Generated by Django 4.1.2 on 2022-10-29 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('resume', models.TextField(blank=True, verbose_name='Опыт работы')),
                ('photo', models.ImageField(max_length=200, upload_to='', verbose_name='Фото')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команда',
                'ordering': ['-created_at'],
            },
        ),
    ]
