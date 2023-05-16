from django.shortcuts import render,redirect
from .models import *
from .forms import *
import random 
x=random.randint(0, 10000)
import datetime
import random 
import time 

now = datetime.datetime.now()
year=datetime.datetime.now().year 
month=datetime.datetime.now().month 
day=datetime.datetime.now().day 
from datetime import date 
today=date.today()


def dashboard(request):
    return render (request,'dashboard.html')
def warehouse(request):
    if request.method == 'POST':
        products=Adddrug.objects.all()
        context={'products':products}
        return render (request,'warehouse.html',context)
    return render (request,'warehouse.html') 


def addproduct(request):
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:warehouse')     
    else:
        form=ProductForm()
    content={
        'form':form
    }
    return render(request,'addproduct.html',content)

# def bill(request):
#     if request.method == 'POST':
#         print('fffff')
#         y=Billsale()

    
#         y.num_bill=request.POST.get('numbill')
#         y.name_of_customer=request.POST.get('name_of_customer')
#         y.allvalue_of_bill=request.POST.get('allvalue_of_bill')
#         y.allvalue_of_bill_after_tax=request.POST.get('allvalue_of_bill_after_tax')
#         y.taken_money  =request.POST.get('taken_money')
#         y.will_taken_money=request.POST.get('will_taken_money')
#         # y.date_of_taken_money=request.POST.get('date_of_taken_money')
#         y.cause=request.POST.get('cause')
#         y.curency=request.POST.get('curency')
#         y.save()
#         x=Product_bills()
#         x.num_bill=request.POST.get('numbill')
#         x.name_of_customer=request.POST.get('name_of_customer')
#         x.name_of_product=request.POST.get('name1')
#         x.unit_of_product=request.POST.get('unit1')
#         x.price_of_unit=request.POST.get('price_unit1')
#         x.num_of_units=request.POST.get('number_unit1')
#         x.price_all=request.POST.get('allmoney1')
#         x.save()
#         print(y)
        

       
  
     

def gill(request):
    if request.method == 'POST':
        import random 
        numbill=random.randint(0, 10000)
        import time 
    
        time2=time.strftime("%H:%M:%S")
        day=time.strftime("%d")
        month=time.strftime("%m")
        year=time.strftime("%Y")
        import datetime 
        date=datetime.date.today()
        # time2=datetime.strftime("%H:%M:%S")
        y=Billsale()

    
        y.num_bill=numbill
        y.name_of_customer=request.POST.get('name_of_customer')
        y.allvalue_of_bill=request.POST.get('allvalue_of_bill')
        y.allvalue_of_bill_after_tax=request.POST.get('allvalue_of_bill_after_tax')
        y.taken_money=request.POST.get('taken_money')
        y.will_taken_money=request.POST.get('will_taken_money')
        y.date_of_taken_money=request.POST.get('date')
        # y.date_of_taken_money=request.POST.get('date_of_taken_money')
        y.cause=request.POST.get('cause')
        y.curency=request.POST.get('curency')
        y.date=date
        y.time=time2
        y.day=day
        y.month=month 
        y.year=year
        y.save()
      
        direction='داخل'
        z=Box()
        z.num_bill=numbill
        z.money=request.POST.get('allvalue_of_bill_after_tax')
        z.direction=direction
        z.date=date
        z.time=time2
        z.day=day
        z.month=month 
        z.year=year
        z.save()
        boxnow=request.POST.get('allvalue_of_bill_after_tax')
        inbox=Boxnow.objects.values('money')
        inb=list(inbox)
        inb1=inb[0]
        inb2=inb1['money']
        inb3=inb2+int(boxnow)
        print(len(inb))
        if len(inb) == 0:
            money=Boxnow()
            money.money=boxnow 
            money.save()
        else:

            Boxnow.objects.all().update(money=inb3)

        num_product1=request.POST.get('number_unit1')
        product_name1=request.POST.get('name1')
        unit1=request.POST.get('unit1')
        num_pb1=Adddrug.objects.filter(product_name=product_name1,unit=unit1).values('num_of_unit')
        tt1=list(num_pb1)
        print(tt1)
        ff1=tt1[0]
        kk1=ff1['num_of_unit']
        gg1=kk1-int(num_product1)
        print(gg1)
        Adddrug.objects.filter(product_name=product_name1,unit=unit1).update(num_of_unit=gg1)
        # print(num_pb)
        x=Product_bills()
        x.num_bill=numbill
        x.name_of_customer=request.POST.get('name_of_customer')
        x.name_of_product=request.POST.get('name1')
        x.unit_of_product=request.POST.get('unit1')
        x.price_of_unit=request.POST.get('price_unit1')
        x.num_of_units=request.POST.get('number_unit1')
        x.price_all=request.POST.get('allmoney1')
        x.date=date
        x.time=time2
        x.day=day
        x.month=month 
        x.year=year
        x.save()
        if request.POST.get('name2') != "":
            x2=Product_bills()
            x2.num_bill=numbill
            x2.name_of_customer=request.POST.get('name_of_customer')
            x2.name_of_product=request.POST.get('name2')
            x2.unit_of_product=request.POST.get('unit2')
            x2.price_of_unit=request.POST.get('price_unit2')
            x2.num_of_units=request.POST.get('number_unit2')
            x2.price_all=request.POST.get('allmoney2')
            x2.date=date 
            x2.time=time2
            x2.day=day
            x2.month=month 
            x2.year=year
            x2.save()
            num_product2=request.POST.get('number_unit2')
            product_name2=request.POST.get('name2')
            unit2=request.POST.get('unit2')
            num_pb2=Adddrug.objects.filter(product_name=product_name2,unit=unit2).values('num_of_unit')
            tt2=list(num_pb2)
            ff2=tt2[0]
            kk2=ff2['num_of_unit']
            gg2=kk2-int(num_product2)
        
            Adddrug.objects.filter(product_name=product_name2,unit=unit2).update(num_of_unit=gg2)
#             print(y)
            if request.POST.get('name3') != "":
                x3=Product_bills()
                x3.num_bill=numbill
                x3.name_of_customer=request.POST.get('name_of_customer')
                x3.name_of_product=request.POST.get('name3')
                x3.unit_of_product=request.POST.get('unit3')
                x3.price_of_unit=request.POST.get('price_unit3')
                x3.num_of_units=request.POST.get('number_unit3')
                x3.price_all=request.POST.get('allmoney3')
                x3.date=date
                x3.time=time2
                x3.day=day
                x3.month=month 
                x3.year=year
                x3.save()
                print(y)
                num_product3=request.POST.get('number_unit3')
                product_name3=request.POST.get('name3')
                unit3=request.POST.get('unit3')
                num_pb3=Adddrug.objects.filter(product_name=product_name3,unit=unit3).values('num_of_unit')
                tt3=list(num_pb3)
                ff3=tt3[0]
                kk3=ff3['num_of_unit']
                gg3=kk3-int(num_product3)
              
                Adddrug.objects.filter(product_name=product_name3,unit=unit3).update(num_of_unit=gg3)
                if request.POST.get('name4') != "":
                    x4=Product_bills()
                    x4.num_bill=request.POST.get('numbill')
                    x4.name_of_customer=request.POST.get('name_of_customer')
                    x4.name_of_product=request.POST.get('name4')
                    x4.unit_of_product=request.POST.get('unit4')
                    x4.price_of_unit=request.POST.get('price_unit4')
                    x4.num_of_units=request.POST.get('number_unit4')
                    x4.price_all=request.POST.get('allmoney4')
                    x4.date=date
                    x4.time=time2
                    x4.day=day
                    x4.month=month 
                    x4.year=year
                    x4.save()
                 
                    num_product4=request.POST.get('number_unit4')
                    product_name4=request.POST.get('name4')
                    unit4=request.POST.get('unit4')
                    num_pb4=Adddrug.objects.filter(product_name=product_name4,unit=unit4).values('num_of_unit')
                    tt4=list(num_pb4)
                    ff4=tt4[0]
                    kk4=ff4['num_of_unit']
                    gg4=kk4-int(num_product4)
                   
                    Adddrug.objects.filter(product_name=product_name4,unit=unit4).update(num_of_unit=gg4)
                    # if request.POST.get('name2') != "":
                    #     x2=Product_bills()
                    #     x2.num_bill=request.POST.get('numbill')
                    #     x2.name_of_customer=request.POST.get('name_of_customer')
                    #     x2.name_of_product=request.POST.get('name2')
                    #     x2.unit_of_product=request.POST.get('unit2')
                    #     x2.price_of_unit=request.POST.get('price_unit2')
                    #     x2.num_of_units=request.POST.get('number_unit2')
                    #     x2.price_all=request.POST.get('allmoney2')
                    #     x2.save()
                    #     print(y)
                    #     if request.POST.get('name2') != "":
                    #         x2=Product_bills()
                    #         x2.num_bill=request.POST.get('numbill')
                    #         x2.name_of_customer=request.POST.get('name_of_customer')
                    #         x2.name_of_product=request.POST.get('name2')
                    #         x2.unit_of_product=request.POST.get('unit2')
                    #         x2.price_of_unit=request.POST.get('price_unit2')
                    #         x2.num_of_units=request.POST.get('number_unit2')
                    #         x2.price_all=request.POST.get('allmoney2')
                    #         x2.save()
                    #         print(y)
                    #         if request.POST.get('name2') != "":

                    #             x2=Product_bills()
                    #             x2.num_bill=request.POST.get('numbill')
                    #             x2.name_of_customer=request.POST.get('name_of_customer')
                    #             x2.name_of_product=request.POST.get('name2')
                    #             x2.unit_of_product=request.POST.get('unit2')
                    #             x2.price_of_unit=request.POST.get('price_unit2')
                    #             x2.num_of_units=request.POST.get('number_unit2')
                    #             x2.price_all=request.POST.get('allmoney2')
                    #             x2.save()
                    #             print(y)
                    #             if request.POST.get('name2') != "":
                    #                 x2=Product_bills()
                    #                 x2.num_bill=request.POST.get('numbill')
                    #                 x2.name_of_customer=request.POST.get('name_of_customer')
                    #                 x2.name_of_product=request.POST.get('name2')
                    #                 x2.unit_of_product=request.POST.get('unit2')
                    #                 x2.price_of_unit=request.POST.get('price_unit2')
                    #                 x2.num_of_units=request.POST.get('number_unit2')
                    #                 x2.price_all=request.POST.get('allmoney2')
                    #                 x2.save()
                    #                 print(y)
                    #                 if request.POST.get('name2') != "":
                    #                     x2=Product_bills()
                    #                     x2.num_bill=request.POST.get('numbill')
                    #                     x2.name_of_customer=request.POST.get('name_of_customer')
                    #                     x2.name_of_product=request.POST.get('name2')
                    #                     x2.unit_of_product=request.POST.get('unit2')
                    #                     x2.price_of_unit=request.POST.get('price_unit2')
                    #                     x2.num_of_units=request.POST.get('number_unit2')
                    #                     x2.price_all=request.POST.get('allmoney2')
                    #                     x2.save()
                    #                     print(y)
                    #                     if request.POST.get('name2') != "":
                    #                         x2=Product_bills()
                    #                         x2.num_bill=request.POST.get('numbill')
                    #                         x2.name_of_customer=request.POST.get('name_of_customer')
                    #                         x2.name_of_product=request.POST.get('name2')
                    #                         x2.unit_of_product=request.POST.get('unit2')
                    #                         x2.price_of_unit=request.POST.get('price_unit2')
                    #                         x2.num_of_units=request.POST.get('number_unit2')
                    #                         x2.price_all=request.POST.get('allmoney2')
                    #                         x2.save()
                    #                         print(y)
                    #                         if request.POST.get('name2') != "":
                    #                             x2=Product_bills()
                    #                             x2.num_bill=request.POST.get('numbill')
                    #                             x2.name_of_customer=request.POST.get('name_of_customer')
                    #                             x2.name_of_product=request.POST.get('name2')
                    #                             x2.unit_of_product=request.POST.get('unit2')
                    #                             x2.price_of_unit=request.POST.get('price_unit2')
                    #                             x2.num_of_units=request.POST.get('number_unit2')
                    #                             x2.price_all=request.POST.get('allmoney2')
                    #                             x2.save()
                                                # print(y)
    return render(request,'kaka.html')
def showproduct(request):
    # if request.method == 'POST':
    products=Adddrug.objects.all()
    context={'products':products}
    return render (request,'showproduct.html',context)
#     # return render (request,'showproduct.html')


def delete_product(request,pk):
    item=Adddrug.objects.get(product_id=pk)
    if request.method == 'POST':


        item.delete()
        return redirect('main:showproduct')
    context={
        'item':item
    }    
    return render(request,'deleteproduct.html',context)    

# فاتورة بيع المستودع الأول   
# def bill(request):


#     return render(request,'bill.html') 


def check_bill(request):
    if request.method == 'POST':
        name_of_customer=request.POST.get('name_of_customer')


        y=Billsale.objects.values('name_of_customer')

        yy=list(y)
        names=[]
      
        for i in yy:
            names.append(i['name_of_customer'])
      
       
      


        if name_of_customer in names:

            num_bill=Billsale.objects.values('num_bill').filter(name_of_customer=name_of_customer)
            yy=list(num_bill)
            t=[]
            for i in yy:
                t.append(i['num_bill'])

            x=Billsale.objects.filter(name_of_customer=name_of_customer) 
            item=Product_bills.objects.filter(name_of_customer=name_of_customer)

           

            context={
            't':t,
                # 'x':x
                } 
            return render(request,'check_bill.html',context)
        else:

            return render(request,'check_bill.html')




    return render(request,'check_bill.html') 


    # x=Billsale.objects.all(products)
    # y=Billsale.objects.all()
    # x=Product_bills.objects.all()
    # context={

    #     'x':x,
    #     'y':y 
    # }
    # y=Billsale.objects.values('num_bill')
    # yy=list(y)
    # t=[]
    # for i in yy:
    #     t.append(i['num_bill']) 
    #     print(t)
    
    #     Billsale.objects.filter(num_bill=i)
    # context={
    #     'y':t
    #         }



    # return render(request,'check_bill.html',context)    
    


def show_bill(request,pk):
    item=Product_bills.objects.filter(num_bill=pk)
    x=Billsale.objects.get(num_bill=pk)    
    context={
        'item':item,
        'x':x
        }    
    return render(request,'showbill.html',context)  


# # صفحة مراجعة الفواتير العامة فيها ازرار (حسب الاسم -حسب الرقم حسب التاريخ)  
def check_bill_general(request):



    return render(request,'check_bill_general.html')  


def check_bill_byname(request):
    if request.method == 'POST':
        name_of_customer=request.POST.get('name_of_customer')


        y=Billsale.objects.values('name_of_customer')

        xx=list(y)
        names=[]
      
        for i in xx:
            names.append(i['name_of_customer'])
      
       
      

        print(names)
        if name_of_customer in names:

            num_bill=Billsale.objects.values('num_bill').filter(name_of_customer=name_of_customer)
            yy=list(num_bill)
            t=[]
            for i in yy:
                t.append(i['num_bill'])

            x=Billsale.objects.filter(name_of_customer=name_of_customer) 
            item=Product_bills.objects.filter(name_of_customer=name_of_customer)

           

            context={
            't':t,
                'x':x
                } 
            return render(request,'check_bill_byname.html',context)
        else:

            return render(request,'check_bill_byname.html')




    return render(request,'check_bill_byname.html') 




def check_bill_bynum(request):
    if request.method == 'POST':
        num_bill=request.POST.get('num_bill')
        y=Billsale.objects.values('num_bill')
        yy=list(y)
        t=[]
      


        for i in yy:
            t.append(i['num_bill'])


        if num_bill in t:

            x=Billsale.objects.get(num_bill=num_bill) 
            item=Product_bills.objects.filter(num_bill=num_bill)

            context={
            'item':item,
            'x':x
            } 
            return render(request,'check_bill_bynum.html',context)
        else:

            return render(request,'check_bill_bynum.html') 
    
    return render(request,'check_bill_bynum.html') 




def check_bill_bydate(request):



    return render(request,'check_bill_bydate.html') 



# #///// دالة حذف دواء بعد عرضه من خلال الاسم 
def delete_product_byname(request,pk):
    item=Product_bills.objects.filter(num_bill=pk)
    item2=Billsale.objects.filter(num_bill=pk) 
    if request.method == 'POST':


        item.delete()
        item2.delete()
        return redirect('main:check_bill')
        context={
        'item':item,
        'item2':item2
            }    
        return render(request,'delete_product_byname.html',context)

    return render(request,'delete_product_byname.html')








# #     return render(request,'delete_product_byname')


def update_bill_byname(request,pk):
    item=Product_bills.objects.filter(num_bill=pk)
    item2=Billsale.objects.get(num_bill=pk)
    print(item)
    print(item2)
    
    name_of_products=Product_bills.objects.values('name_of_product').filter(num_bill=pk)
    yy=list(name_of_products)
    t=[]
   

    name_of_customer=item2.name_of_customer
    allvalue_of_bill=item2.allvalue_of_bill
    allvalue_of_bill_after_tax=item2.allvalue_of_bill_after_tax 
    taken_money=item2.taken_money
    will_taken_money=item2.will_taken_money
    date=item2.date  
    time=item2.time
    day=item2.day
    month=item2.month
    year=item2.year
    for i in yy:
        t.append(i['name_of_product']) 

    print(item2)
    # if request.method == 'POST':

    context={
            'item':item ,
            'name_of_customer':name_of_customer,
            'allvalue_of_bill':allvalue_of_bill,
            'allvalue_of_bill_after_tax':allvalue_of_bill_after_tax , 
           ' taken_money':taken_money ,
           'will_taken_money':will_taken_money
            }     
    
    if request.method =='POST':

        
        name_of_product1=request.POST.get('name1')
        if name_of_product1 in t and name_of_product1 != "" :

            unit_of_product1=request.POST.get('unit1')
            price_of_unit1=request.POST.get('price_unit1')
            num_of_units1=request.POST.get('number_unit1')
            price_all1=request.POST.get('allmoney1')
     
            Product_bills.objects.filter(num_bill=pk, name_of_product=name_of_product1,unit_of_product=unit_of_product1).update(num_of_units=num_of_units1,price_of_unit=price_of_unit1,price_all=price_all1)
        elif name_of_product1 not in t and name_of_product1 != "":
            x1=Product_bills()
            x1.num_bill=pk
            x1.name_of_product=request.POST.get('name1')
            x1.unit_of_product=request.POST.get('unit1')
            x1.price_of_unit=request.POST.get('price_unit1')
            x1.num_of_units=request.POST.get('number_unit2')
            x1.price_all=request.POST.get('allmoney2')
            x1.date=date 
            x1.time=time
            x1.day=day
            x1.month=month 
            x1.year=year
            x1.save()        


       
        num_bill=request.POST.get('numbill')
        name_of_customer=request.POST.get('name_of_customer')
        allvalue_of_bill=request.POST.get('allvalue_of_bill')
        allvalue_of_bill_after_tax=request.POST.get('allvalue_of_bill_after_tax')
        taken_money=request.POST.get('taken_money')
        will_taken_money=request.POST.get('will_taken_money')
        date_of_taken_money=request.POST.get('date')
        cause=request.POST.get('cause')
        curency=request.POST.get('curency')
        date=date
        time=time
        day=day
        month=month 
        year=year
     
        Billsale.objects.filter(num_bill=pk, name_of_customer=name_of_customer
        ).update(num_bill=pk,allvalue_of_bill=allvalue_of_bill
       ,allvalue_of_bill_after_tax=allvalue_of_bill_after_tax)


        # return render(request,'update_product_byname.html',context)

    return render(request,'update_product_byname.html',context)








# صغحة المبيعات

def sales(request):


    return render (request,'sales.html') 

# رؤية المبيعات في يوم محدد   
def showsalesday(request):
    if request.method =='POST':

        date=request.POST.get('date')
        item=Product_bills.objects.filter(date=date)
        item2=Product_bills.objects.values('price_all').filter(date=date)
        yy=list(item2)
        t=[]
        for i in yy:
            t.append(i['price_all'])

        x=0 
        for i in t:
            x+= i    

        context={
            'item':item ,
            'x': x
        }
        return render (request,'showsalesinday.html',context)

    return render (request,'showsalesinday.html') 



def showsalesmonth(request):
    if request.method =='POST':

        month=request.POST.get('month')
        year=request.POST.get('year')
        item=Product_bills.objects.filter(month=month,year=year)
        item2=Product_bills.objects.values('price_all').filter(month=month,year=year)
        yy=list(item2)
        t=[]
        for i in yy:
            t.append(i['price_all'])

        x=0 
        for i in t:
            x+= i  
        context={
            'item':item ,
             'x':x
        }
        return render (request,'showsalesinmonth.html',context)




    return render (request,'showsalesinmonth.html') 



def showsalesyear(request):
    if request.method =='POST':

    
        year=request.POST.get('year')
        item=Product_bills.objects.filter(year=year)
        item2=Product_bills.objects.values('price_all').filter(year=year)
        yy=list(item2)
        t=[]
        for i in yy:
            t.append(i['price_all'])

        x=0 
        for i in t:
            x+= i  
        context={
            'item':item,
            'x':x
        }
        return render (request,'showsalesinyear.html',context)




    return render (request,'showsalesinyear.html') 



# صفحة الصندوق    ////// 
def box (request):


    return render (request,'box.html') 



# عرض حركة الصندوق في يوم محدد
def boxday(request):
    if request.method =='POST':
        date=request.POST.get('date')
        item=Box.objects.filter(date=date) 
        context={
            'item':item
        }

        return render (request,'boxday.html',context)
    return render (request,'boxday.html')

def boxmonth(request):
    if request.method =='POST':
        month=request.POST.get('month')
        year=request.POST.get('year')
        item=Box.objects.filter(month=month,year=year) 
        context={
            'item':item
        }

        return render (request,'boxmonth.html',context)
    return render (request,'boxmonth.html')   
def boxnow (request):
    item=Boxnow.objects.values('money')
    inb=list(item)
    inb1=inb[0]
    inb2=inb1['money'] 
    context={
        'item':inb2
        }


    return render(request,'boxnow.html',context)  



def expenses(request):
    if request.method == 'POST':
        form=Sarf(request.POST)
        if form.is_valid():
            form.save()
            inbox=Boxnow.objects.values('money')
            money=request.POST.get('money')
            inb=list(inbox)
            inb1=inb[0]
            inb2=inb1['money']
            inb3=inb2-int(money)
            print(len(inb))
            if len(inb) == 0:
                money=Boxnow()
                money.money=boxnow 
                money.save()
            else:

                Boxnow.objects.all().update(money=inb3)
            import time 
    
            time2=time.strftime("%H:%M:%S") 
            day=time.strftime("%d")
            month=time.strftime("%m")
            year=time.strftime("%Y")
            import datetime 
            date=datetime.date.today()   
            direction='خارج'
            z=Box()
            z.num_bill=request.POST.get('num_bill')
            z.money=request.POST.get('money')
            z.direction=direction
            z.date=date
            z.day=day 
            z.month=month 
            z.year=year
            z.time=time2
        
            z.save() 
           

            return redirect('main:warehouse')     
    else:
        form=Sarf()
    context={
        'form':form
    }





    return render(request,'expenses.html',context) 



# صفحة فواتير الصرف العامة     
def expensesg(request):




    return render(request,'expensesg.html') 

# //////   مراجعة فواتيى الصرف  
def checkexpenses(request):
    if request.method == 'POST':
        numbill=request.POST.get('numbill')
        item=Expense.objects.filter(num_bill=numbill)
        context={

            'item':item
        }


        return render(request,'check_expenses.html', context) 

    return render(request,'check_expenses.html') 


# دالة حذف فاتورة صرف 
def deleteexpense(request,pk):
    item=Expense.objects.filter(num_bill=pk)

    if request.method == 'POST':

        item1=Expense.objects.values('money').filter(num_bill=pk)

        item2=Box.objects.filter(num_bill=pk)
        item3=Boxnow.objects.values('money')
        inb=list(item3)
        inb1=inb[0]
        inb2=inb1['money'] 
        money=list(item1)
        print(money)
        money1=money[0]
        money2=money1['money']

       
        item.delete()
        item2.delete()

        inb3=inb2+money2
         
        if len(inb) == 0:
            money=Boxnow()
            money.money=boxnow 
            money.save()
        else:

            Boxnow.objects.all().update(money=inb3)
        return redirect('main:checkexpenses')    
    context={
        'item':pk,
      
            }    
    return render(request,'delete_expense.html',context)



