# Generated by Django 5.0.1 on 2024-01-08 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_mashina_kuzov_alter_mashina_manzil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mashina',
            name='Yana',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.yana'),
        ),
    ]
