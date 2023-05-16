from django.db import models 
from django.utils.text import slugify 
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
import random 
import time 
from django.utils import timezone
# from datetime import datetime
import datetime

k=datetime.datetime.now()
x=str(random.randint(0,10000))

year=datetime.datetime.now().year 
month=datetime.datetime.now().month 
day=datetime.datetime.now().day 
from datetime import date 
today=date.today()
# Create your models here.
#      كلاس إضافة دواء        
class Adddrug(models.Model):
    product_id = models.AutoField(primary_key=True)
    time=models.TimeField(_("التوقيت"), auto_now=1, )

    product_name = models.CharField(max_length=100,verbose_name=_('اسم المنتج'))
    category = models.CharField(max_length=100, default="",verbose_name=_('الفئة'))
    desc = models.CharField(max_length=500,verbose_name=_('الوصف'))
    currency=models.CharField(max_length=500,verbose_name=_('العملة'))
    unit=models.CharField(max_length=100,null=True,blank=True,verbose_name=_('الوحدة'))
    num_of_unit=models.IntegerField(default=0,null=True,blank=True,verbose_name=_('عدد الوحدات'))

    cost_of_unit = models.IntegerField(default=0,null=True,blank=True,verbose_name=('تكلفة الوحدة'))
    price_of_unit = models.IntegerField(default=0,null=True,blank=True,verbose_name=('سعر الوحدة'))
   
    date_of_entering=models.DateField(default=timezone.now,verbose_name=_('تاريخ الإدخال'))

    date_of_ending=models.DateField(verbose_name=_('تاريخ انتهاء الصلاحية'))
    
    image = models.ImageField(upload_to='photoproduct/%y/%m/%d',null=True,blank=True,verbose_name=_('صورة المنتج'))
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.product_name 
   
    
       
    class Meta :
        verbose_name=_('drug')
        verbose_name_plural=_('drugs')

#     قاعدة بيانات الفاتورة للمستودع الأول 







     

class Billsale(models.Model):

    num_bill=models.CharField(max_length=100,verbose_name=_('رقم الفاتورة'))
    name_of_customer=models.CharField(max_length=100,verbose_name=_('اسم المشتري'))
    allvalue_of_bill=models.IntegerField(verbose_name=_('قيمة الفاتورة الكلية'))
    allvalue_of_bill_after_tax=models.IntegerField(verbose_name=_(' قيمة الفاتورة الكلية مع الضريبة '))

    taken_money=models.IntegerField(verbose_name=_('المبلغ المقبوض'))
    will_taken_money=models.IntegerField(verbose_name=_('المبلغ المتبقي'),blank=True,null=True)
    cause=models.TextField(verbose_name=_('السبب'),blank=True,null=True)
    date_of_taken_money=models.DateField(verbose_name=_('وقت استرداد المال'),blank=True,null=True)
    curency=models.CharField(max_length=100,verbose_name=_('العملة'),blank=True,null=True)
    date=models.DateField(_("التاريخ"), default=k)
    day=models.CharField(max_length=100,verbose_name=_("اليوم"))
    month=models.CharField(max_length=100,verbose_name=_("الشهر")) 
    year=models.CharField(max_length=100,verbose_name=_("السنة"))
    time=models.TimeField(_("التوقيت") )
    # products=models.ForeignKeyField(Product_bill, verbose_name=_(" المنتجات"))  
    def __str__(self):
        return self.num_bill




class Product_bills(models.Model):
        
    num_bill=models.CharField(max_length=100,verbose_name=_('رقم الفاتورة'))
    name_of_customer=models.CharField(max_length=100,verbose_name=_('اسم المشتري'))

    name_of_product=models.CharField(max_length=100,verbose_name=_('اسم المنتج'))
    unit_of_product=models.CharField(max_length=100,verbose_name=_('الوحدة'))
    price_of_unit=models.IntegerField(verbose_name=_('سعر الوحدة'))
    num_of_units=models.IntegerField(verbose_name=_('العدد'))
    price_all=models.IntegerField(verbose_name=_('القيمة'))
    date=models.DateField(_("التاريخ"), default=k)
    day=models.CharField(max_length=100,verbose_name=_("اليوم"))
    month=models.CharField(max_length=100,verbose_name=_("الشهر")) 
    year=models.CharField(max_length=100,verbose_name=_("السنة"))
    time=models.TimeField(_("التوقيت") )




# الصندوق //////// 

class Box(models.Model):
    money=models.IntegerField(verbose_name=_('المال الداخل'))
    direction=models.CharField(max_length=100,verbose_name=_('الاتجاه'))
    date=models.DateField(_('التاريخ'))
    day=models.CharField(max_length=100,verbose_name=_("اليوم"))
    month=models.CharField(max_length=100,verbose_name=_("الشهر")) 
    year=models.CharField(max_length=100,verbose_name=_("السنة"))
    time=models.TimeField(_("التوقيت") )

    num_bill=models.CharField(max_length=100,verbose_name=_('رقم الفاتورة')) 
    


#////// الصندوق حالياً  //////// 
class Boxnow (models.Model):
    

    money=models.IntegerField(verbose_name=_('المال الموحود حالياً')) 



class Expense(models.Model) :
    num_bill=models.CharField(max_length=100,verbose_name=_('رقم الفاتورة'),default=x)
    typebill=models.CharField(max_length=100,verbose_name=_('نوع الفاتورة'))
    money=models.IntegerField(verbose_name=_('المبلغ')) 
    date=models.DateField(_('التاريخ'))
    time=models.TimeField(_("التوقيت") )

    