from django.contrib import admin
from .models import DeliveryChallan, Invoice, PurchaseOrder,  Quote

# Register DeliveryChallan, Invoice, and PurchaseOrder models
admin.site.register(DeliveryChallan)
admin.site.register(Invoice)
admin.site.register(PurchaseOrder)


admin.site.register(Quote)