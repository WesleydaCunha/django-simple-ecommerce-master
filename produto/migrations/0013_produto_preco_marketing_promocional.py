# Generated by Django 5.0.6 on 2024-06-27 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0012_remove_produto_preco_marketing_promocional_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(default=0, verbose_name='Preço Promo.'),
        ),
    ]
