from django.db import models
from .validators import validate_file_extension

class DeliveryChallan(models.Model):
    dc_number = models.CharField(max_length=100)
    image = models.ImageField(upload_to='dc_images/', validators=[validate_file_extension])
    description = models.CharField(max_length=1000)
    dc_date = models.DateField()
    department = models.CharField(max_length=100)
    total_amount = models.IntegerField()
    is_grn = models.BooleanField(default=False)
    po = models.ForeignKey('PurchaseOrder', on_delete=models.CASCADE)

    def __str__(self):
        return self.dc_number

class Quote(models.Model):
    quote_number = models.CharField(max_length=100)
    quote_img = models.ImageField(upload_to='quote_images/', validators=[validate_file_extension])
    description = models.CharField(max_length=1000)
    event_date = models.DateField()
    quote_date = models.DateField()
    participants = models.IntegerField(default=0)
    department = models.CharField(max_length=100)
    total_amount = models.IntegerField()
    is_po_approved= models.BooleanField(default=False)
    po = models.ForeignKey('PurchaseOrder', on_delete=models.CASCADE)

    def __str__(self):
        return self.quote_number + ' - ' + self.po.po_number

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100)
    image = models.ImageField(upload_to='invoice_images/', validators=[validate_file_extension])
    description = models.CharField(max_length=1000)
    invoice_date = models.DateField()
    sent_date = models.DateField(blank=True, null=True)
    department = models.CharField(max_length=100)
    total_amount = models.IntegerField()
    is_sent = models.BooleanField(default=False)
    po = models.ForeignKey('PurchaseOrder', on_delete=models.CASCADE)
    is_amount_received = models.BooleanField(default=False)

    def __str__(self):
        return self.invoice_number
    




class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    po_date = models.DateField()
    department = models.CharField(max_length=100)
    po_amount = models.IntegerField()
    grn_amount = models.IntegerField(default=0)
    po_remaining_amount = models.IntegerField(blank=True, null=True)
    dc = models.ManyToManyField(DeliveryChallan, null=True, blank=True)
    invoices = models.ManyToManyField(Invoice, null=True, blank=True)

    def __str__(self):
        return self.po_number
    
   
      




        


