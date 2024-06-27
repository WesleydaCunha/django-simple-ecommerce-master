# Generated by Django 5.0.6 on 2024-06-26 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0010_alter_variacao_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variacao',
            options={'verbose_name': 'Variação', 'verbose_name_plural': 'Variações'},
        ),
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('A', 'ALUGUEL'), ('D', 'DOAÇÃO')], default='A', max_length=1),
        ),
    ]
