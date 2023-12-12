from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from courses.models import Course
from . forms import ContactForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from teachers.models import Teacher

# Create your views here.

class IndexViews(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['courses'] = Course.objects.filter(avaliable = True).order_by('-date')[:2]

        context['total_course'] = Course.objects.filter(avaliable = True).count()
        
        context['total_students'] = User.objects.count()
        
        context['total_teachers'] = Teacher.objects.count()
        
        return context



class AboutViews(TemplateView):
    template_name = 'about.html'

class ContactViews(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    
    form_class = ContactForm

    success_url = reverse_lazy('contact') # İlgili url'e döner

    success_message = 'We received your request'


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

