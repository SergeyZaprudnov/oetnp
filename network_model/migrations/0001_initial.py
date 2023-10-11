# Generated by Django 4.2.6 on 2023-10-11 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование товара')),
                ('model', models.CharField(max_length=150, verbose_name='Модель товара')),
                ('release_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('email', models.EmailField(max_length=150, verbose_name='Электронная почта')),
                ('country', models.CharField(max_length=150, verbose_name='Страна')),
                ('city', models.CharField(max_length=150, verbose_name='Город')),
                ('street', models.CharField(max_length=150, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=150, verbose_name='Номер дома')),
                ('hierarchy', models.IntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], max_length=150, verbose_name='Уровень звена')),
                ('debt', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Задолженность')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('product', models.ManyToManyField(to='network_model.product', verbose_name='Товары')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='network_model.structure', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Структура сети',
                'verbose_name_plural': 'Структуры сети',
            },
        ),
    ]