# Generated by Django 5.0.1 on 2024-01-06 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_narxi_narxi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rasm',
            name='rasm',
            field=models.ImageField(blank=True, null=True, upload_to='media/rasm/', verbose_name='rasm'),
        ),
        migrations.AlterField(
            model_name='tortishi',
            name='tortsh',
            field=models.CharField(blank=True, choices=[('Polniy', 'Polniy'), ('Orqa', 'Orqa')], max_length=50, null=True),
        ),
    ]
