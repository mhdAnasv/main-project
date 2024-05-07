from django.shortcuts import render


def appointments(request):
    return render(request,'appointment.html')

# def booking(request):
#     if (request.method == "POST"):
#         u = request.POST['u']
#         f = request.POST["f"]
#         p = request.POST["p"]
#         e = request.POST["e"]
#         dt = request.POST["dt"]
#         st = request.POST["st"]
#         tr = request.POST["tr"]
#
#
#
#
#     return render(request, "appointment.html",name="booking")

def register(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")

