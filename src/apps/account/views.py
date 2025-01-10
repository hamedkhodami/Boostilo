from django.shortcuts import render
from django.views.generic import ListView
from .models import ProfileTeam

# Create your views here.

def accountest(request):
    return render(request,"account/signup.html")

class TeamListView(ListView):
    model = ProfileTeam
    template_name = ''
    context_object_name = 'team_members'

    def get_queryset(self):
        return ProfileTeam.objects.all()


class TeamPhotoListView(ListView):
    model = ProfileTeam
    template_name = ''
    context_object_name = 'photo_members'

    def get_queryset(self):
        return ProfileTeam.objects.only("photo").filter(photo__isnull=False)[:6]




