from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def function_template_view(request):
    return render(request,'second_task/func_template.html')

class ClassTemplateView(TemplateView):
    def get(self, request):
        return render(request, 'second_task/class_template.html')
