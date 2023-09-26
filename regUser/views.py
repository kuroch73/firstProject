from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.db import IntegrityError



def  regUserView(request):
    if request.method == "GET":
        return render(request, 'regUser/regUser.html', {'formuser' : UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
                return render(request, 'regUser/regUser.html', {'formuser': UserCreationForm()})
            except IntegrityError:
                error = "Это имя уже используется"
                return render(request, 'regUser/regUser.html', {'formuser': UserCreationForm(),'error': error })

        else:

            error = "Пароли должны совпадать"
            return render(request, 'regUser/regUser.html', {'formuser': UserCreationForm(), 'error': error })

def logoutuserview(request):
    logout(request)
    return redirect('home')

def questionnaireView(request):
    foto = request.GET.get('foto')
    firstname = request.GET.get('firstname')
    lastname = request.GET.get('lastname')
    birth = request.GET.get('birth')
    skill_1 = request.GET.get('skill_1')
    skill_2 = request.GET.get('skill_2')
    skill_3 = request.GET.get('skill_3')
    skill_4 = request.GET.get('skill_4')
    skill_5 = request.GET.get('skill_5')
    about = request.GET.get('about')
    context = {
        'foto_html': foto,
        'firstname_html': firstname,
        'lastname_html': lastname,
        'birth_html': birth,
        'skill_1_html': skill_1,
        'skill_2_html': skill_2,
        'skill_3_html': skill_3,
        'skill_4_html': skill_4,
        'skill_5_html': skill_5,
        'about_html': about,
    }
    return render(request, template_name='questionnaire.html',context=context)
def loginUserView(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'reguser/loginuser.html', {'form' : form})
    else:
        form = AuthenticationForm(request.POST)
        user = authenticate(username = request.POST['username'], password=request.POST['password'])
        try:
            login(request,user)
            return redirect('home')
        except:
            return render(request, 'regUser/loginuser.html', {'form' : form ,'errors': 'Неверный логин или пароль'})
def logoutuserview(request):
    logout(request)
    return redirect('home')
