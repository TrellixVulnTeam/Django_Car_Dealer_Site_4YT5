from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Araba(models.Model):
    arabaismi = models.CharField(max_length=120,verbose_name='ARAÇ ADI')
    modeli = models.IntegerField(default=2018,verbose_name='MODEL YILI')
    kilometre = models.IntegerField(default=0,verbose_name='KİLOMETRE')
    fiyat = models.IntegerField(default=0,verbose_name='FİYAT(TL)')
    silindirhacmi = models.IntegerField(default=1000,verbose_name='SİLİNDİR HACMİ')
    yakit = models.CharField(
        choices=(('BENZİN', 'BENZİN'),('LPG/BENZİN', 'LPG/BENZİN'),('DİZEL', 'DİZEL'),('HİBRİT', 'HİBRİT'),),default='benzin' ,verbose_name='YAKIT TÜRÜ',max_length=15)
    vites = models.CharField(
        choices=(('MANUEL', 'MANUEL'),('OTOMATİK', 'OTOMATİK'),),default='manuel' ,verbose_name='VİTES TİPİ',max_length=15)
    renk = models.CharField(max_length=25,verbose_name='RENK', default='')
    ozellikler = models.TextField(verbose_name='ÖZELLİKLER')
    ilantarihi = models.DateTimeField(verbose_name='iLAN TARİHİ',auto_now_add='True')
    foto1= models.ImageField(null='True', blank = 'True',verbose_name='1.FOTOĞRAF(VİTRİN)')
    foto2= models.ImageField(null='True', blank = 'True',verbose_name='2.FOTOĞRAF')
    foto3= models.ImageField(null='True', blank = 'True',verbose_name='3.FOTOĞRAF')
    foto4= models.ImageField(null='True', blank = 'True',verbose_name='4.FOTOĞRAF')
    foto5= models.ImageField(null='True', blank = 'True',verbose_name='5.FOTOĞRAF')



    def __str__ (self):#admin panelinde başlığı gösterme
        return self.arabaismi

    def datepublished(self):#sadece tarihi gösterme
        return self.ilantarihi.strftime(' %d/%m/%y ')

    class Meta:
        ordering=['-ilantarihi']
