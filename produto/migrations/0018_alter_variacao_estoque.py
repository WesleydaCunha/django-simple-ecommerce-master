# Generated by Django 5.0.6 on 2024-06-27 01:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0017_rename_quantidade_dias_variacao_quandidade_dias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variacao',
            name='estoque',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
    ]
