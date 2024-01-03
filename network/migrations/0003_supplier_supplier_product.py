# Generated by Django 5.0 on 2024-01-03 08:11

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='supplier',
            field=models.CharField(choices=[('self-employed', 'ИП'), ('retailer', 'розничная сеть')], default=None, verbose_name='Тип поставщика'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('released', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата выхода продукта на рынок')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.manufacturer', verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]