# Generated by Django 5.0.4 on 2024-07-08 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_deliverychallan_image_alter_invoice_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverychallan',
            name='grn_id',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='invoice',
            name='dc',
            field=models.ManyToManyField(to='main.deliverychallan'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='grn_id',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='po_creater',
            field=models.CharField(default='PTC', max_length=100),
        ),
    ]