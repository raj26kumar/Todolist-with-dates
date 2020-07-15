from django.shortcuts import render , redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from . models import List



# Create your views here.

def home(request):
    item = request.POST.get('item')
    date = request.POST.get('date')
    
    if item=="":
        messages.error(request, "Type something in your wish-list")
        all_items = List.objects.all
        return render(request,'home.html',{'all_items': all_items}) 

    elif date=="" :
        messages.error(request, "select date")
        all_items = List.objects.all
        return render(request,'home.html',{'all_items': all_items})   

    else:

        if request.method == 'POST':
            form = ListForm(request.POST or None)

            if form.is_valid():
                form.save()
                all_items = List.objects.all
                messages.success(request, ('Added to Wish List '))
                return render(request, 'home.html', {'all_items': all_items})
            
        else:
            all_items = List.objects.all
            return render(request,'home.html',{'all_items': all_items})       

    
       

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item deleted'))
    return redirect('home')




