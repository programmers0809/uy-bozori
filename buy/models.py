from django.utils import timezone 
from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Kategoriya nomi')
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Kategoriya '
        verbose_name_plural = 'Kategoriyalar'
        db_table = 'Categorys'
        managed = True

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='Faol')

class HouseModel(models.Model):
    
    class Status(models.TextChoices):
        Deactive = 'Faol emas', 'Faol emas'
        Active = 'Faol', 'Faol'
        
    
    UZ = "so'm"
    RU = '₽'
    ENG = '$'

    the_price = (
        (UZ, "so'm"),
        (RU, "₽"),
        (ENG, "$"),
    )

    address = models.CharField(max_length=255, verbose_name='Adres')
    price = models.IntegerField(verbose_name='Narxi')
    price_type = models.CharField(max_length=10, choices=the_price, default="$")
    area = models.PositiveIntegerField(verbose_name='Kvadrat metri')
    floor = models.CharField(max_length=20, verbose_name='Qavati')
    parking = models.CharField(max_length=50, verbose_name ='Avtoturargohi')
    image = models.ImageField(upload_to='homes/images', verbose_name='Rasmi')
    category = models.ForeignKey(CategoryModel,
                                        verbose_name="Kategoriyasi",
                                        on_delete=models.CASCADE)
    
    publish_time = models.DateTimeField(default=timezone.now, verbose_name='Yangiliklar yaratilgan vaqti')
    created_time = models.DateTimeField(auto_now_add=True) 
    updated_time = models.DateTimeField(auto_now=True) 
    status = models.CharField(max_length=50,
                                    choices=Status.choices,
                                    default=Status.Deactive,
                                    verbose_name='holati'
                                    )
    
    
    
    objects = models.Manager ()
    manager = ActiveManager()
    
    class Meta:
        ordering = ['-publish_time']
        db_table = 'houses'
        managed = True
        verbose_name = 'Uy'
        verbose_name_plural = 'Uylar'

    def __str__(self):
        return f"{self.category} - {self.address}"


