from django.shortcuts import render
from django.http import HttpResponse
#from models import Aritcle

# Create your views here.

def index(request):
    return HttpResponse("Hello.world.You're at the app01 index.")

def detail(request,question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request,question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s." % question_id)

#def year_archive(request,year):
#    a_list = Article.objects.filter(pub_date__year=year)
#    context = {'year':year,'article_list':a_list}
#    return render(request,'news/year_archive.html',context)
