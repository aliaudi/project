from django.urls import path 
from . import views 
app_name='main'

urlpatterns = [
 
    path('',views.dashboard,name='dashboard'),
    path('warehouse',views.warehouse,name='warehouse'),
    path('addproduct',views.addproduct,name='addproduct'),
    # path('bill',views.bill,name='bill'),
    path('gill',views.gill,name="gill"),
    # path('gill',views.gill,name="gill"),
    path('showproduct',views.showproduct,name='showproduct'),
    path('deleteproduct/<int:pk>',views.delete_product,name='deleteproduct'),
    path('deleteproduct_name/<int:pk>',views.delete_product_byname,name='delete_product_byname'),
    path('updatebill_name/<int:pk>',views.update_bill_byname,name='updatebill'),

    path('showbill/<int:pk>',views.show_bill,name='showbill'),

    # path('bill',views.bill,name="bill"),
    path('check_bill',views.check_bill,name="check_bill"), 
    path('check_bill_byname',views.check_bill_byname,name="check_bill_byname"), 
    path('check_bill_bynum',views.check_bill_bynum,name="check_bill_bynum"), 
    path('check_bill_bydate',views.check_bill_bydate,name="check_bill_bydate"),

    path('check_bill_general',views.check_bill_general,name="check_bill_general"),
    path('sales',views.sales,name="sales"),
    path('showsalesday',views.showsalesday,name="showsalesday"),
    path('showsalesmonth',views.showsalesmonth,name="showsalesmonth"),
    path('showsalesyear',views.showsalesyear,name="showsalesyear"),
    path('box',views.box, name="box"),
    path('boxday',views.boxday, name="boxday"),
    path('boxmonth',views.boxmonth, name="boxmonth"),
    path('boxnow',views.boxnow, name="boxnow"),
    path('expenses',views.expenses,name="expenses"),
    path('expensesg',views.expensesg,name="expensesg"),
    path('checkexpenses',views.checkexpenses,name="checkexpenses"),
    path('deleteexpense/<int:pk>',views.deleteexpense,name="deleteexpense"),


]
