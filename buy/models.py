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

