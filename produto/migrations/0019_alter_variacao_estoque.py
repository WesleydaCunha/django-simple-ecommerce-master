# Generated by Django 5.0.6 on 2024-06-27 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0018_alter_variacao_estoque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variacao',
            name='estoque',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
