from django.shortcuts import render, redirect
from .models import escaperoom
# Create your views here.



def delete(request, pk):
    x = escaperoom.objects.get(id=pk)
    x.delete()
    return redirect('/')

def index(request):

    escaperoom_list = escaperoom.objects.all()  #getting list of escaperoom

    if request.method == 'POST':
        new_item = escaperoom(
            escaperoom_name = request.POST['title']
        )
        new_item.save()
        return redirect('/')

    return render(request, 'index.html', {'escaperooms': escaperoom_list})

