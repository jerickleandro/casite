# Generated by Django 3.0.2 on 2020-01-29 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20200129_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='membros',
            name='descricao',
            field=models.TextField(default='SOME STRING', verbose_name='Descrição'),
        ),
    ]
