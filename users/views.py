from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout
from users.forms import AuthenticationForm
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login_view') # на главную страницу сайта

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login_view.html'
    form_class = AuthenticationForm
    
    def get_success_url(self):
        return reverse_lazy('home') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Неверный логин или пароль')
        return self.render_to_response(self.get_context_data(form=form))
    