from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from users.forms import AuthenticationForm


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login_view.html'
    form_class = AuthenticationForm
    
    def get_success_url(self):
        return reverse_lazy('home') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Неверный логин или пароль')
        return self.render_to_response(self.get_context_data(form=form))
    