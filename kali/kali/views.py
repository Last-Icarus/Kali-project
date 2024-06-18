from django.shortcuts import render
from .models import Art, Commission, User, UserSettings
from django.http import HttpResponse
from .forms import ImageForm, ArtForm, ArtFormSet

def login_page(request):
    return render(request, 'login.html')

def home(request):
    arts = Art.objects.all()
    context = {"arts" : arts}
    return render(request, 'home.html', context)

def commissions(request):
    commissions = Art.objects.all()
    context = {'commissions' : commissions}
    return render(request, 'commissions.html', context)

def profile(request, user_id):
    user = User.objects.get(id=user_id)
    try:
        settings = UserSettings.objects.get(user=user)
    except:
        UserSettings.objects.create(user=user)
        settings = UserSettings.objects.get(user=user)

    if request.method == 'POST':

        if 'avatar' in request.FILES:
            settings.avatar = request.FILES['avatar']
        if 'header' in request.FILES:
            settings.header = request.FILES['header']
        if 'bio' in request.POST:
            settings.bio = request.POST['bio']
        if 'no_ai_tag' in request.POST:
            settings.no_ai_tag = bool(request.POST['no_ai_tag'])
        settings.save()
                
    user_arts = Art.objects.filter(author=user_id)
    user_commissions = Commission.objects.filter(author=user_id)
    context = {'user' : user, 'user_arts' : user_arts, 'user_commissions' : user_commissions, 'form' : ImageForm, 
               'user_settings' : settings }
    return render(request, 'profile.html', context)

def studio(request):
    user = User.objects.get(id = request.user.id)
    arts = Art.objects.filter(author = user)
    commissions = Commission.objects.filter(author = user)
    context = {'arts' : arts, 'commissions' : commissions}
    return render(request, 'studio.html', context)

def create_art(request):  
    if request.method == 'POST':
        postres = request.POST
        files = request.FILES
        Art.objects.create(name=postres['art_name'],
                        description=postres['description'],
                        image=files['art_image_1'],
                        author=User.objects.get(id=request.user.id))
    else:
        return render(request, 'create_art.html', {'form' : ArtFormSet})

def create_commission(request):
    print(request.POST)
    return render(request, 'create_commission.html')
