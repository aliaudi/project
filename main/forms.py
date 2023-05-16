from django import forms 
from .models import * 




# /////فورم إضافة دواء
class ProductForm(forms.ModelForm):
    class Meta:
        model=Adddrug 
        fields=['product_name','category','desc','unit','num_of_unit',
        'price_of_unit','cost_of_unit',
         'date_of_entering','date_of_ending','image','currency']


#  //////قائمة إضافة أمر صرف /////
class Sarf(forms.ModelForm):
    class Meta:
        model=Expense
        fields=['num_bill','typebill','money','date','time']