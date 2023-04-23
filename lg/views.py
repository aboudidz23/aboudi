from django.shortcuts import render

from lg.models import secret

# Create your views here.
def index(request):
    
    user = request.POST.get('user')
    password = request.POST.get('password')
    data = secret(user=user , password=password)
    if request.method == 'POST':
        data.save()
    return render(request , 'index.html')