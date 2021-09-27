from django.db import models
from django.core.exceptions import ValidationError
from django.dispatch import receiver

# Create your models here.

class Product(models.Model):
    product_id = models.CharField(max_length=16, primary_key=True)
    product_name = models.CharField(max_length=64)

    def __str__(self):
        return self.product_id

class Location(models.Model):
    location_id = models.CharField(max_length=16, primary_key=True)
    location_name = models.CharField(max_length=64)

    def __str__(self):
        return self.location_id

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

class ProductMovement(models.Model):
    movement_id = models.CharField(max_length=16, primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    from_location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.CASCADE, related_name='from_location')
    to_location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.CASCADE, related_name='to_location')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def clean(self, *args, **kwargs):
        
        if not (self.from_location or self.to_location):
            raise ValidationError('Both from and to cannot be blank.')

        if self.from_location == self.to_location:
            raise ValidationError('From and to location cannot be same.')


        if self.from_location:
            stock = Stock.objects.get_or_create(location=self.from_location, product=self.product)[0]
            diff = stock.quantity - self.quantity
            try:
                movement = ProductMovement.objects.get(pk=self.pk)
                diff += movement.quantity
            except:
                pass
            if diff < 0:
                raise ValidationError('Not enough stock available.')

        super(ProductMovement, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):

        if self.to_location:
            stock = Stock.objects.get_or_create(location=self.to_location, product=self.product)[0]
            stock.quantity += self.quantity
            try:
                movement = ProductMovement.objects.get(pk=self.pk)
                stock.quantity -= movement.quantity
            except self.DoesNotExist:
                pass
            stock.save()
        
        if self.from_location:
            stock = Stock.objects.get_or_create(location=self.from_location, product=self.product)[0]
            diff = stock.quantity - self.quantity
            try:
                movement = ProductMovement.objects.get(pk=self.pk)
                diff += movement.quantity
            except:
                pass
            if diff < 0:
                raise ValidationError('Not enough stock available.')
            stock.quantity = diff
            stock.save()

        return super(ProductMovement, self).save( *args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.to_location:
            stock = Stock.objects.get_or_create(location=self.to_location, product=self.product)[0]
            stock.quantity -= self.quantity
            stock.save()
        
        if self.from_location:
            stock = Stock.objects.get_or_create(location=self.from_location, product=self.product)[0]
            diff = stock.quantity + self.quantity
            stock.quantity = diff
            stock.save()

        return super(ProductMovement, self).delete(*args, **kwargs)



    def __str__(self):
        return self.movement_id