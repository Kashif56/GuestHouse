from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('po-list/', views.po_list, name='po_list'),
    path('po-list/po/<po_number>/', views.po_detail_page, name='po_detail_page'),
    path('form/po-form/', views.po_form_page, name='po_form'),
    path('form/PO-form/edit/<po_number>/', views.edit_po, name='edit_po'),
    path('POs/delete/<po_number>/', views.delete_po, name='delete_po'),
   

    path('quotes-list/', views.quotes_list, name='quote_list'),
    path('quotes-list/quote/<quote_number>/', views.quote_detail_page, name='quote_detail_page'),
    path('form/quote-form/', views.quote_form_page, name='quote_form'),
    path('form/quote-form/edit/<quote_number>/', views.edit_quote, name='edit_quote'),
    path('quotes/delete/<quote_number>/', views.delete_quote, name='delete_quote'),
  

    path('dc-list/', views.dc_list, name='dc_list'),
    path('dc-list/dc/<dc_number>/', views.dc_detail_page, name='dc_detail_page'),
    path('form/dc-form/', views.dc_form_page, name='dc_form'),
    path('form/dc-form/edit/<dc_number>/', views.edit_dc, name='edit_dc'),
    path('DCs/delete/<dc_number>/', views.delete_dc, name='delete_dc'),
    

    path('invoice-list/', views.invoice_list, name='invoice_list'),
    path('invoice-list/invoice/<invoice_number>/', views.invoice_detail_page, name='invoice_detail_page'),
    path('form/invoice-form/', views.invoice_form_page, name='invoice_form'),
    path('form/invoice-form/edit/<invoice_number>/', views.edit_invoice, name='edit_invoice'),
    path('invoices/delete/<invoice_number>/', views.delete_invoice, name='delete_invoice'),

    path('po/<po_number>/grn_dc/', views.grn_dc, name='grn_dc'),
    path('po/<dc_number>/grn_inv/', views.grn_inv, name='grn_inv'),


    path('departments/', views.department_list, name='dept_list'),
   
]