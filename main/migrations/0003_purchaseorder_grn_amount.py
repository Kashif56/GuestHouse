# Generated by Django 5.0.4 on 2024-04-27 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='grn_amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]