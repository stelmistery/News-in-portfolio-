from django.shortcuts import render, get_object_or_404, redirect
from .models import Category

# Create your views here.


def cat_list(request):
    cats = Category.objects.all()
    return render(request, 'back/cat_list.html', {'cats': cats})


def cat_add(request):

    if request.method == 'POST':
        name = request.POST.get('name')

        if name == '':
            error = 'All fields required'
            return render(request, 'back/error.html', {'error': error})

        c = Category(name=name)
        c.save()
        return redirect('cat_list')

    return render(request, 'back/cat_add.html')

