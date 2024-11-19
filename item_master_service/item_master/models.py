from django.db import models

class Item_master(models.Model):
    status=models.IntegerField(default=1)
    stampdatetime=models.DateField(auto_now=True)
    item_name = models.TextField(max_length=50)
    rate      = models.PositiveIntegerField()
    def __str__(self):
        return self.item_name
    class  Meta:
        db_table = 'item_master'

#         {
#     "status": "1",
#     "stampdatetime": "2024-11-19",
#     "item_name": 'Laptop',
#     "rate": 20
# }