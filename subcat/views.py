from django.shortcuts import render, get_object_or_404, redirect
from .models import SubCategory
from cat.models import Category
# Create your views here.


def subcat_list(request):
    subcats = SubCategory.objects.all()
    return render(request, 'back/subcat_list.html', {'subcats': subcats})


def subcat_add(request):

    cats = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        catid = request.POST.get('cat')

        if name == '':
            error = 'All fields required'
            return render(request, 'back/error.html', {'error': error})

        if len(SubCategory.objects.filter(name=name)) != 0:
            error = 'This Name Used Before'
            return render(request, 'back/error.html', {'error': error})

        catname = Category.objects.get(pk=catid).name

        sc = SubCategory(name=name, catname=catname, catid=catid)
        sc.save()
        return redirect('subcat_list')

    return render(request, 'back/subcat_add.html', {'cats': cats})

