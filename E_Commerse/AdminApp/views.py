from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.conf import settings
from E_Commerse.models import Customer,ProductDetail,ProductImage
#for logout
from django.contrib.auth import logout

curl = settings.C_URL
media_url=settings.MEDIA_URL

#for file uploading
from django.core.files.storage import FileSystemStorage

# Create your views here.
def sessioncheckadmin_middleware(get_response):
    def middleware(request):
        print("============= request=====:",request.path)
        strpath = request.path
        list1 = strpath.split("/")
        if len(list1)>2:
            strnewpath = "/"+list1[1]+"/"+list1[2]+"/"
            if strnewpath=='/ecommerseadmin/home/' or strnewpath=='/ecommerseadmin/managecustomer/' or strnewpath=='/ecommerseadmin/addproduct/' or strnewpath == '/ecommerseadmin/addproductimage/' or strnewpath == '/ecommerseadmin/changepassword/' or strnewpath == '/ecommerseadmin/editprofile/' :
                if 'emailid' not in request.session:            
                    response=redirect('http://localhost:8000/login')
                else:
                    response=get_response(request)
            else:
                response=get_response(request)
        else:
            return get_response(request)        
        return response
        
    return middleware 



def home(request):
    #==============session
    emailid=request.session.get("emailid")
    password=request.session.get("password")
    #==============session 
    qs=Customer.objects.filter(email=emailid,password=password).values("name","email","mobile","address")
    print(qs[0])
    return render(request,'AdminHome.html',{'curl':curl,'data':qs[0]})

def addproduct(request):
    if request.method == "GET":
        return render(request,'AddProduct.html',{'curl':curl})
    elif request.method == "POST":
        p_brand=request.POST.get("p_brand")
        p_price=request.POST.get("p_price")
        p_old_price=request.POST.get("p_old_price")
        p_discount=request.POST.get("p_discount")
        p_size=request.POST.get("p_size")
        p_description=request.POST.get("p_description")
        p_quantity=request.POST.get("p_quantity")
        p_availability=request.POST.get("p_availability")

        print(p_brand,p_price,p_old_price,p_discount,p_size,p_description,p_quantity,p_availability)
        msg=""
        try:
            add_prod_detail=ProductDetail(product_brand=p_brand,product_price=p_price,product_old_price=p_old_price,product_discount=p_discount,product_size=p_size,product_description=p_description,product_quantity=p_quantity,product_availability=p_availability)
            add_prod_detail.save()
            msg="Product Added Successfully!!"
        except:  
            msg="Product Not Added !!"
  
        return render(request,'AddProduct.html',{'curl':curl,"msg":msg})

def changepassword(request):
    return render(request,'ChangePassword.html',{'curl':curl})

def editprofile(request):
    return render(request,'EditProfile.html',{'curl':curl})

def addproductimage(request):
    if request.method == "GET":
        qs=ProductDetail.objects.all().values("product_id","product_brand")
        print(qs)
        return render(request,'AddProductImage.html',{'curl':curl,"listofproduct":qs})
    elif request.method == "POST":
        product_id=request.POST.get("product_id")
        print(product_id)
        files = request.FILES.getlist('product_img')
        print(files)
        file_list = [] 
        msg=""
        try:  
            prod_detail = ProductDetail.objects.get(product_id=product_id)
            print(prod_detail)
            for file in files:
                #for file uploading .............................
                fs=FileSystemStorage()
                fs.save(file.name,file)  
                #....................................................
                new_file = ProductImage(product_img=file,product_id=prod_detail)
                new_file.save()
                file_list.append(new_file.product_img)
            msg="Product Images Uploaded Successfully"  
        except:
            msg="Product Images Not Uploaded!!"      

        return render(request,'AddProductImage.html',{'curl':curl,"msg":msg,'new_url':str(new_file.product_img),'list_img':file_list})    
    '''
    elif request.method == "POST":
        product_id=request.POST.get("product_id")
        print(product_id)
        #for file uploading .............................
        product_img1=request.FILES["product_img"]
        print(product_id,product_img1)
        fs=FileSystemStorage()
        fs.save(product_img1.name,product_img1)  
        #....................................................
        prod_detail = ProductDetail.objects.get(product_id=product_id)
        print(prod_detail)
        msg=""
        try:
            prod_img=ProductImage(product_img=product_img1,product_id=prod_detail)
            prod_img.save()
            msg="Product Image Uploaded Successfully"
        except:
            msg="Product Image Not Uploaded!!"    
        return render(request,'AddProductImage.html',{'curl':curl,"msg":msg})
    '''    

def managecustomer(request):
    customers=Customer.objects.filter(role="customer").values()
    print(customers)
    return render(request,'ManageCustomer.html',{'curl':curl,'customers':customers})

def managecustomerstatus(request):
    if request.method=="GET":
        id=request.GET.get('id')
        status=request.GET.get('status')
        print(id,status)
        if status == "0":
           Customer.objects.filter(customer_id=id).update(status=1)
           
        elif status == "1":
           Customer.objects.filter(customer_id=id).update(status=0)
          
        return redirect(curl+'ecommerseadmin/managecustomer/')    

def deletecustomer(request):
    if request.method=="GET":
        id=request.GET.get('id')
        print("Customer Id:",id)
        Customer.objects.filter(customer_id=id).delete()
        return redirect(curl+'ecommerseadmin/managecustomer/') 

def Logout(request):
    logout(request)
    return redirect('http://localhost:8000/login/')
