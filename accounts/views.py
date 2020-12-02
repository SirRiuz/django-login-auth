
# Django 
from django.shortcuts import (render , redirect)
from django.contrib.auth import (authenticate , login as login_method)

# Forms 
from .forms import (LoginForm,RegisterForm)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            email = form.data['email']
            password = form.data['password']

            user = authenticate(request=request ,email=email , password=password)

            if user != None:
                login_method(request , user)
                return redirect(to='/')
        
            else:
                return render(
                    request,
                    template_name='login.html',
                    context=({
                        'error':True
                    })
                )    

    if request.user.is_authenticated:
        return redirect(to='/')


    return render(
        request,
        template_name='login.html'
    )



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST , request.FILES)
        if form.is_valid():
            print('Formulario valido')

        else:
            print('ERROR EN EL FORMULARIO')
            return render(
                request=request,
                template_name='register.html',
                context={
                    'form_error':True
                }
            )
    return render(
        request=request,
        template_name='register.html'
    )