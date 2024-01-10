from django.shortcuts import render
from django.http import HttpResponse
from .models import News,Journal, Team, Category, Research




def home(request):
    posts = News.objects.all().order_by('-date_posted')[:3]
    display_news = News.objects.filter(display=True)

    context = {
        'posts':posts,
        'display_news':display_news
    }
    return render(request,'mars/index.html',context)
# Create your views here.
def people(request):
    display_news = News.objects.filter(display=True)
    teams =  Team.objects.all()

    post_scholars =  [team for team in teams if team.category == 'POST' and team.status == 'CURRENT']
    research_scholars = [team for team in teams if team.category == 'DOC' and team.status == 'CURRENT']
    mtech_scholars = [team for team in teams if team.category == 'MTECH' and team.status == 'CURRENT']
    btech_scholars = [team for team in teams if team.category == 'BTECH' and team.status == 'CURRENT']
    project_scholars = [team for team in teams if team.category == 'PS' and team.status == 'CURRENT']

    context = {
        'research_scholars': research_scholars,
        'project_scholars': project_scholars,
        'post_scholars': post_scholars,
        'mtech_scholars':mtech_scholars,
        'btech_scholars':btech_scholars,
        'display_news':display_news,
    }
    return render(request,'mars/people.html', context)

def alumni(request):
    display_news = News.objects.filter(display=True)
    teams =  Team.objects.all()

    post_scholars =  [team for team in teams if team.category == 'POST' and team.status == 'ALLUMNI']
    research_scholars = [team for team in teams if team.category == 'DOC' and team.status == 'ALLUMNI']
    mtech_scholars = [team for team in teams if team.category == 'MTECH' and team.status == 'ALLUMNI']
    btech_scholars = [team for team in teams if team.category == 'BTECH' and team.status == 'ALLUMNI']
    project_scholars = [team for team in teams if team.category == 'PS' and team.status == 'ALLUMNI']

    context = {
        'research_scholars': research_scholars,
        'project_scholars': project_scholars,
        'post_scholars': post_scholars,
        'mtech_scholars':mtech_scholars,
        'btech_scholars':btech_scholars,
        'display_news':display_news
    }
    return render(request,'mars/alumni.html', context)

def infrastructure(request):
    display_news = News.objects.filter(display=True)

    context ={
        'display_news':display_news
    }
    return render(request,'mars/infrastructure.html',context)

def research(request):
    display_news = News.objects.filter(display=True)
    researchs = Research.objects.all()

    Ongoing =  [research for research in researchs if research.researchtype == 'og' ]
    completed = [research for research in researchs if research.researchtype == 'comp' ]

    context ={
        'ongoing': Ongoing,
        'completed':completed,
        'display_news':display_news
    }
    return render(request,'mars/research.html',context)

def publications(request):
     display_news = News.objects.filter(display=True)
    
     journal ={
         'journals':Journal.objects.all(),
         'display_news':display_news
     }
     
     return render(request,'mars/publications.html',journal)

def news(request):
    display_news = News.objects.filter(display=True)
    context = {
        'posts':News.objects.all().order_by('-date_posted'),
        'display_news':display_news
    }
    return render(request,'mars/news.html',context)

def gallery(request):
    display_news = News.objects.filter(display=True)
    categories = Category.objects.all()

    context ={
        'display_news':display_news,
        'categories': categories
    }
    
    return render(request,'mars/gallery.html', context)

def video(request):
    return render(request,'mars/video.html')


