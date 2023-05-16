# Generated by Django 4.2 on 2023-05-06 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billsale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_bill', models.CharField(default='6127', max_length=100, verbose_name='رقم الفاتورة')),
                ('name_of_customer', models.CharField(max_length=100, verbose_name='اسم المشتري')),
                ('allvalue_of_bill', models.IntegerField(verbose_name='قيمة الفاتورة الكلية')),
                ('allvalue_of_bill_after_tax', models.IntegerField(verbose_name=' قيمة الفاتورة الكلية مع الضريبة ')),
                ('taken_money', models.IntegerField(verbose_name='المبلغ المقبوض')),
                ('will_taken_money', models.IntegerField(blank=True, null=True, verbose_name='المبلغ المتبقي')),
                ('cause', models.TextField(blank=True, null=True, verbose_name='السبب')),
                ('date_of_taken_money', models.DateField(blank=True, null=True, verbose_name='وقت استرداد المال')),
                ('cuurency', models.CharField(blank=True, max_length=100, null=True, verbose_name='العملة')),
                ('name_of_product1', models.CharField(max_length=100, verbose_name='اسم المنتج')),
                ('unit_of_product1', models.CharField(max_length=100, verbose_name='الوحدة')),
                ('price_of_unit1', models.IntegerField(verbose_name='سعر الوحدة')),
                ('num_of_units1', models.IntegerField(verbose_name='العدد')),
                ('price_all1', models.IntegerField(verbose_name='القيمة')),
                ('time_of_bill', models.TimeField(auto_now=1, verbose_name='وقت الفاتورة')),
                ('date_of_bill', models.DateField(auto_now=True, verbose_name='تاريخ الفاتورة')),
            ],
        ),
        migrations.AlterField(
            model_name='adddrug',
            name='date_of_entering',
            field=models.DateField(default=datetime.datetime(2023, 5, 6, 9, 58, 13, 506087), verbose_name='تاريخ الإدخال'),
        ),
    ]
