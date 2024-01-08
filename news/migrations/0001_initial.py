# Generated by Django 5.0.1 on 2024-01-05 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kuzov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turi', models.CharField(choices=[('Sedan', 'Sedan'), ('Xetchbek', 'Xetchbek'), ('Universal', 'Universal'), ('Kabriolet', 'Kabriolet'), ('Krossover', 'Krossover'), ('Kupe', 'Kupe'), ('Limuzin', 'Limuzin'), ('Mikroavtobus', 'Mikroavtobus'), ('Miniven', 'Miniven'), ('Mikroven', 'Mikroven'), ('Pikap', 'Pikap'), ('Rodster', 'Rodster'), ('Furgon', 'Furgon')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Manzil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manzl', models.CharField(choices=[('Andijon', 'Andijon'), ('Namangan', 'Namangan'), ('Surhandaryo', 'Surxandaryo'), ('Qashqadaryo', 'Qashqadaryo'), ('Fargona', 'Fargona'), ('Toshkent', 'Toshkent'), ('Buxoro', 'Buxoro')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Narxi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narxi', models.IntegerField(help_text='MASHINA_NARXI', verbose_name='narxi')),
            ],
        ),
        migrations.CreateModel(
            name='Obyom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obyom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Peredacha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peredacha', models.CharField(choices=[('mexanika', 'mexanika'), ('avtomat', 'avtomat'), ('tiptronik', 'tiptronik'), ('variator', 'variator'), ('robot', 'robot')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rasm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='media/rasm/', verbose_name='rasm')),
            ],
        ),
        migrations.CreateModel(
            name='Rusumi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('marka', models.CharField(choices=[('BMW', 'BMW'), ('Mers', 'Mersedez_Benz'), ('Porsh', 'Porsh'), ('Doj', 'Dodge'), ('Lambor.', 'Lamborghini')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tortishi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tortsh', models.CharField(choices=[('Polniy', 'Polniy'), ('Orqa', 'Orqa')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Turi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Yengil', 'Yengil'), ('Ogir', 'Ogir')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Yana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Yili',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yili', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Yoqilgi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mashina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Kuzov', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news.kuzov')),
                ('Manzil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news.manzil')),
                ('Narxi', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news.narxi')),
                ('Obyom', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news.obyom')),
                ('Peredacha', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news.peredacha')),
                ('Rang', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news.rang')),
                ('rasm', models.ManyToManyField(to='news.rasm')),
                ('Rusumi', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.rusumi')),
                ('Tortishi', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news.tortishi')),
                ('Turi', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news.turi')),
                ('Yana', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news.yana')),
                ('yili', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news.yili')),
                ('Yoqilgi', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news.yoqilgi')),
            ],
        ),
    ]
