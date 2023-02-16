from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'main/index.html'

class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'

def lab1(request):
    return render(request, 'layouts/default/lab1.html')

def profile(request):
    return render(request, 'layouts/default/profile.html')




