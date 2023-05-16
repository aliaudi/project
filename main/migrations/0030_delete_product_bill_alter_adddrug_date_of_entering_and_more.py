# Generated by Django 4.2 on 2023-05-09 02:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_billsale_product_bill_alter_adddrug_date_of_entering'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product_bill',
        ),
        migrations.AlterField(
            model_name='adddrug',
            name='date_of_entering',
            field=models.DateField(default=datetime.datetime(2023, 5, 8, 21, 49, 43, 649511), verbose_name='تاريخ الإدخال'),
        ),
        migrations.AlterField(
            model_name='billsale',
            name='num_bill',
            field=models.CharField(default='2539', max_length=100, verbose_name='رقم الفاتورة'),
        ),
    ]