from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def trangchu(request):
    return render(
            request=request,
            template_name="banhang/trangchu.html",
            )
