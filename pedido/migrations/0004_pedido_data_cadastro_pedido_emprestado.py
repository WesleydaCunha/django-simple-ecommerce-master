# Generated by Django 5.0.6 on 2024-06-26 22:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_pedido_qtd_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='data_cadastro',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='pedido',
            name='emprestado',
            field=models.BooleanField(default=False),
        ),
    ]
