# Generated by Django 4.2.5 on 2024-01-08 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_mashina_rasm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mashina',
            name='Rusumi',
        ),
        migrations.AddField(
            model_name='mashina',
            name='rusumi',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.rusumi'),
        ),
    ]
