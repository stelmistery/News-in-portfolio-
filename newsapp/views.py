from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.core.files.storage import FileSystemStorage

# Create your views here.


def article_detail(request, word):
    article = Article.objects.get(name=word)
    return render(request, 'main/article.html', {'article': article})


def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'back/articles_list.html', {'articles': articles})


def articles_add(request):
    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')

        if newstitle == "" or newscat == "" or newstxtshort == "" or newstxt == "":
            errors = "All fields required"
            return render(request, 'back/error.html', {'errors': errors})

        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if str(myfile.content_type).startswith('image'):
                if myfile.size > 5000000:
                    article = Article(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, catid=0, catname=newscat, date=2019, picname=filename, picurl=url, writer='-')
                    article.save()
                    return redirect('articles_add')
                else:
                    error = "Your file size is bigger than 5MB"
                    return render(request, 'back/error.html', {'error': error})
            else:
                error = "Your file NOT supported"
                return render(request, 'back/error.html', {'error': error})


        except:
            error = "Please input your image"
            return render(request, 'back/error.html', {'error': error})

    return render(request, 'back/articles_add.html')
