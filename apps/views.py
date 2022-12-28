from django.views.generic import DetailView,  TemplateView

from .models import *


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutUser.objects.first()
       # context['projects'] = Project.objects.all()
        context['skills'] = Skill.objects.all()
        context['services'] = Service.objects.all()
        context['educations'] = Education.objects.all()

        return context


class ProjectDetailView(DetailView):

    template_name = "project-details.html"
    queryset = Project.objects.all()
    context_object_name = 'project'

