# Generated by Django 5.0.6 on 2024-06-27 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0013_produto_preco_marketing_promocional'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variacao',
            old_name='quantidade_dias',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='variacao',
            name='nome',
        ),
    ]
