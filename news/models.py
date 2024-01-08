from django.db import models


class Rusumi(models.Model):
    mark = (
        ('BMW', 'BMW'),
        ('Mers', 'Mersedez_Benz'),
        ('Porsh', 'Porsh'),
        ('Doj', 'Dodge'),
        ('Lambor.', 'Lamborghini'),
    )
    name = models.CharField(max_length=250)
    marka = models.CharField(max_length=50, choices=mark)

    def __str__(self):
        return f"{self.name}-->{self.marka}"


class Tortishi(models.Model):
    tortishi = (
        ("Polniy", "Polniy"),
        ("Orqa", "Orqa"),
    )
    tortsh = models.CharField(max_length=50, choices=tortishi, null=True, blank=True)

    def __str__(self):
        return self.tortsh


class Kuzov(models.Model):
    tur = (
        ('Sedan', 'Sedan'),
        ('Xetchbek', 'Xetchbek'),
        ('Universal', 'Universal'),
        ('Kabriolet', 'Kabriolet'),
        ('Krossover', 'Krossover'),
        ('Kupe', 'Kupe'),
        ('Limuzin', 'Limuzin'),
        ('Mikroavtobus', 'Mikroavtobus'),
        ('Miniven', 'Miniven'),
        ('Mikroven', 'Mikroven'),
        ('Pikap', 'Pikap'),
        ('Rodster', 'Rodster'),
        ('Furgon', 'Furgon'),
    )
    turi = models.CharField(max_length=50, choices=tur)

    def __str__(self):
        return self.turi


class Yili(models.Model):
    yili = models.CharField(max_length=4)

    def __str__(self):
        return self.yili


class Obyom(models.Model):
    obyom = models.CharField(max_length=50)

    def __str__(self):
        return self.obyom


class Peredacha(models.Model):
    peredach = (
        ('mexanika', 'mexanika'),
        ('avtomat', 'avtomat'),
        ('tiptronik', 'tiptronik'),
        ('variator', 'variator'),
        ('robot', 'robot'),
    )
    peredacha = models.CharField(max_length=50, choices=peredach)

    def __str__(self):
        return self.peredacha


class Rang(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Turi(models.Model):
    tur = (
        ('Yengil', 'Yengil'),
        ('Ogir', 'Ogir'),
    )
    name = models.CharField(max_length=50, choices=tur)

    def __str__(self):
        return self.name


class Rasm(models.Model):
    rasm = models.ImageField(verbose_name='rasm', upload_to='media/rasm/', null=True, blank=True)

    def __str__(self):
        return str(self.rasm)


class Yoqilgi(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Narxi(models.Model):
    narxi = models.IntegerField(verbose_name='narxi', help_text='MASHINA_NARXI', null=True, blank=True)

    def __str__(self):
        return str(self.narxi)


class Yana(models.Model):
    content = models.TextField()


class Manzil(models.Model):
    manzil = (
        ('Andijon', 'Andijon'),
        ('Namangan', 'Namangan'),
        ('Surhandaryo', 'Surxandaryo'),
        ('Qashqadaryo', 'Qashqadaryo'),
        ('Fargona', 'Fargona'),
        ('Toshkent', 'Toshkent'),
        ('Buxoro', 'Buxoro'),
    )
    manzl = models.CharField(max_length=50, choices=manzil)

    def __str__(self):
        return self.manzl


class Mashina(models.Model):
    rusumi = models.ForeignKey(Rusumi, on_delete=models.CASCADE, null=True, blank=True)
    Yoqilgi = models.ForeignKey(Yoqilgi, on_delete=models.CASCADE, null=True, blank=True)
    Narxi = models.ForeignKey(Narxi, on_delete=models.CASCADE, null=True, blank=True)
    Manzil = models.ForeignKey(Manzil, on_delete=models.CASCADE, null=True, blank=True)
    Turi = models.ForeignKey(Turi, on_delete=models.CASCADE, null=True, blank=True)
    Yana = models.OneToOneField(Yana, on_delete=models.CASCADE, null=True, blank=True)
    rasm = models.ManyToManyField(Rasm)
    Rang = models.ForeignKey(Rang, on_delete=models.CASCADE, null=True, blank=True)
    Peredacha = models.ForeignKey(Peredacha, on_delete=models.CASCADE, null=True, blank=True)
    Obyom = models.ForeignKey(Obyom, on_delete=models.CASCADE, null=True, blank=True)
    yili = models.ForeignKey(Yili, on_delete=models.CASCADE, null=True, blank=True)
    Kuzov = models.ForeignKey(Kuzov, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.Kuzov}--{self.Yoqilgi}"
