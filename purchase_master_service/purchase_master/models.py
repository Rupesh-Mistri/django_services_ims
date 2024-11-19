
from django.db import models

# Create your models here.
class Purchase_master(models.Model):
    invoice_no=models.IntegerField()
    invoice_date=models.DateField()
    supplier_id =models.BigIntegerField()
    status=models.IntegerField(default=1)
    purchase_date=models.DateField(auto_now=True)
    
    class  Meta:
        db_table = 'purchase_master'



class Temp_purchase_details(models.Model):
    status=models.IntegerField(default=1)
    stampdatetime=models.DateField(auto_now=True)
    item_id =models.IntegerField()
    rate=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
    total=models.DecimalField(max_digits=10,decimal_places=2)

    class  Meta:
        db_table = 'temp_purchase_details'


class Purchase_details(models.Model):
    status=models.IntegerField(default=1)
    stampdatetime=models.DateField(auto_now=True)
    item =models.BigIntegerField()
    rate=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
    total=models.DecimalField(max_digits=10,decimal_places=2)
    fkey =models.ForeignKey(Purchase_master,  on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return str(self.item_id)

    class  Meta:
        db_table = 'purchase_details'
    