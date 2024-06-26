from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=55, unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'Катерию'
        verbose_name_plural = 'Категории'

class Products(models.Model):
    name = models.CharField(max_length=55, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, verbose_name='Описание', null=True)
    image = models.ImageField(upload_to='products_images', blank=True, null=True, verbose_name='Фото')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'

    def display_id(self):
        return f'{self.id:05}'

    def total_price(self):
        if self.discount > 0:
            return round(self.price - (self.price * self.discount / 100), 2)
        else:
            return self.price

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['id']