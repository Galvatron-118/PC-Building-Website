from django.shortcuts import render,redirect
from . import models
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings






#######################################################################################################################
########################################### Fetching components from Database #########################################
#######################################################################################################################



#CPU card view
def home_view(request):
    products=models.cpu.objects.all()
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    
    return render(request,'index.html',{'products':products,'product_count_in_cart':product_count_in_cart})

#Motherboard card view
def motherboard_view(request):
    products=models.motherboard.objects.all()
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    
    return render(request,'motherboard.html',{'products':products,'product_count_in_cart':product_count_in_cart})

#CPUcooler card view
def cpucooler_view(request):
    products=models.cpucooler.objects.all()
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    
    return render(request,'cpucooler.html',{'products':products,'product_count_in_cart':product_count_in_cart})

#Case card view
def case_view(request):
    products=models.case.objects.all()
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    
    return render(request,'case.html',{'products':products,'product_count_in_cart':product_count_in_cart})

#Memory card view
def memory_view(request):
    products=models.memory.objects.all()
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    
    return render(request,'memory.html',{'products':products,'product_count_in_cart':product_count_in_cart})

#PowerSupply card view
def powersupply_view(request):
    products=models.powersupply.objects.all()
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    
    return render(request,'powersupply.html',{'products':products,'product_count_in_cart':product_count_in_cart})

#Storage card view
def storage_view(request):
    products=models.storage.objects.all()
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    
    return render(request,'storage.html',{'products':products,'product_count_in_cart':product_count_in_cart})

#VideoCard card view
def videocard_view(request):
    products=models.videocard.objects.all()
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    
    return render(request,'videocard.html',{'products':products,'product_count_in_cart':product_count_in_cart})






################################################################################################
####################################### Search Views ###########################################
################################################################################################





def search_view_cpu(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    products=models.cpu.objects.all().filter(name__icontains=query)
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # word variable will be shown in html when user click on search button
    word="Searched Result :"
    
    return render(request,'index.html',{'products':products,'word':word,'product_count_in_cart':product_count_in_cart})

def search_view_motherboard(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    products=models.motherboard.objects.all().filter(name__icontains=query)
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # word variable will be shown in html when user click on search button
    word="Searched Result :"
    
    return render(request,'motherboard.html',{'products':products,'word':word,'product_count_in_cart':product_count_in_cart})

def search_view_cpucooler(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    products=models.cpucooler.objects.all().filter(name__icontains=query)
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # word variable will be shown in html when user click on search button
    word="Searched Result :"
    
    return render(request,'cpucooler.html',{'products':products,'word':word,'product_count_in_cart':product_count_in_cart})

def search_view_case(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    products=models.case.objects.all().filter(name__icontains=query)
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # word variable will be shown in html when user click on search button
    word="Searched Result :"
   
    return render(request,'case.html',{'products':products,'word':word,'product_count_in_cart':product_count_in_cart})

def search_view_memory(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    products=models.memory.objects.all().filter(name__icontains=query)
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # word variable will be shown in html when user click on search button
    word="Searched Result :"

    
    return render(request,'memory.html',{'products':products,'word':word,'product_count_in_cart':product_count_in_cart})

def search_view_powersupply(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    products=models.powersupply.objects.all().filter(name__icontains=query)
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # word variable will be shown in html when user click on search button
    word="Searched Result :"
    
    return render(request,'powersupply.html',{'products':products,'word':word,'product_count_in_cart':product_count_in_cart})

def search_view_storage(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    products=models.storage.objects.all().filter(name__icontains=query)
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # word variable will be shown in html when user click on search button
    word="Searched Result :"
    
    return render(request,'storage.html',{'products':products,'word':word,'product_count_in_cart':product_count_in_cart})

def search_view_videocard(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    products=models.videocard.objects.all().filter(name__icontains=query)
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # word variable will be shown in html when user click on search button
    word="Searched Result :"
    
    return render(request,'videocard.html',{'products':products,'word':word,'product_count_in_cart':product_count_in_cart})


    
    






#################################################################################################
########################################### Cart ###############################################
#################################################################################################



# list of products in cart
def cart_view(request):
    #for cart counter
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # fetching product details from db whose id is present in cookie
    products=None
    
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart=product_ids.split('|')
            products=models.cpu.objects.all().filter(id__in = product_id_in_cart)

            #for total price shown in cart
            for p in products:
                total=total+p.price
    return render(request,'cart.html',{'products':products, 'total':total,'product_count_in_cart':product_count_in_cart})

# list of products in cart
def cart_view_motherboard(request):
    #for cart counter
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=-1

    # fetching product details from db whose id is present in cookie
    
    products=None
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart=product_ids.split('|')
            products=models.motherboard.objects.all().filter(id__in=product_id_in_cart)

            #for total price shown in cart
            for p in products:
                total=total+p.price
    return render(request,'cart.html',{'products':products, 'total':total,'product_count_in_cart':product_count_in_cart})









#################################################################################################
######################################## Add to Cart ############################################
#################################################################################################




def add_to_cart_view(request,pk):
    products=models.cpu.objects.all()

    #for cart counter, fetching products ids from cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    response = render(request, 'finalhtml.html',{'products':products,'product_count_in_cart':product_count_in_cart})

    #adding product id to cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids=="":
            product_ids=str(pk)
        else:
            product_ids=product_ids+"|"+str(pk)
        response.set_cookie('product_ids', product_ids)
    else:
        response.set_cookie('product_ids', pk)

    products=models.cpu.objects.get(id=pk)

    return response




def add_to_cart_view_motherboard(request,pk):
    products=models.motherboard.objects.all()

    #for cart counter, fetching products ids from cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    response = render(request, 'finalhtml.html',{'products':products,'product_count_in_cart':product_count_in_cart})

    #adding product id to cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids=="":
            product_ids=str(pk)
        else:
            product_ids=product_ids+"|"+str(pk)
        response.set_cookie('product_ids', product_ids)
    else:
        response.set_cookie('product_ids', pk)

    products=models.motherboard.objects.get(id=pk)

    return response



"""def addbutton(request):
    products=models.cpu.objects.all()
    mb=models.motherboard.objects.all()

    #for cart counter, fetching products ids added by customer from cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    response = render(request, 'finalhtml.html',{'products':products,'product_count_in_cart':product_count_in_cart})

    #adding product id to cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids=="":
            product_ids=str(pk)
        else:
            product_ids=product_ids+"|"+str(pk)
        response.set_cookie('product_ids', product_ids)
    else:
        response.set_cookie('product_ids', pk)

    products=models.cpu.objects.get(id=pk)
    mb=models.motherboard.objects.get(id=pk)

    return render(request, 'finalhtml.html', {'cpu':products, 'motherboard':mb})

    return response"""










#################################################################################################
######################################### Remove from Cart ######################################
#################################################################################################



def remove_from_cart_view(request,pk):
    #for counter in cart
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # removing product id from cookie
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        product_id_in_cart=product_ids.split('|')
        product_id_in_cart=list(set(product_id_in_cart))
        product_id_in_cart.remove(str(pk))
        products=models.cpu.objects.all().filter(id__in = product_id_in_cart)
        #for total price shown in cart after removing product
        for p in products:
            total=total+p.price

        #  for update coookie value after removing product id in cart
        value=""
        for i in range(len(product_id_in_cart)):
            if i==0:
                value=value+product_id_in_cart[0]
            else:
                value=value+"|"+product_id_in_cart[i]
        response = render(request, 'cart.html',{'products':products,'total':total,'product_count_in_cart':product_count_in_cart})
        if value=="":
            response.delete_cookie('product_ids')
        response.set_cookie('product_ids',value)
        return response
    

def remove_from_cart_view_mb(request,pk):
    #for counter in cart
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # removing product id from cookie
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        product_id_in_cart=product_ids.split('|')
        product_id_in_cart=list(set(product_id_in_cart))
        product_id_in_cart.remove(str(pk))
        products=models.motherboard.objects.all().filter(id__in = product_id_in_cart)
        #for total price shown in cart after removing product
        for p in products:
            total=total+p.price

        #  for update coookie value after removing product id in cart
        value=""
        for i in range(len(product_id_in_cart)):
            if i==0:
                value=value+product_id_in_cart[0]
            else:
                value=value+"|"+product_id_in_cart[i]
        response = render(request, 'cart.html',{'products':products,'total':total,'product_count_in_cart':product_count_in_cart})
        if value=="":
            response.delete_cookie('product_ids')
        response.set_cookie('product_ids',value)
        return response







#######################################################################################
######################################### Signup ######################################
#######################################################################################































#--------------for discharge patient bill (pdf) download and printing
import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return

