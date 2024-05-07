from django.shortcuts import render
# from shop.models import Services,Treatments
def home(request):
    return render(request,"base.html")

def allservices(request):

    return render(request, 'services.html')

# def alltreatment(request,p):
#     c = Services.objects.get(name=p)
#     p = Treatments.objects.filter(category=c)
#     return render(request, 'treatments.html', {'c': c, 'p': p})

def alltreatment(request):
    # c = Services.objects.get(name=p)
    # p = Treatments.objects.filter(category=c)
    return render(request, 'treatments.html')

def allproducts(request):
    return render(request,"products.html")