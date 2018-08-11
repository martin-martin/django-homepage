import random
from django.shortcuts import render
from .models import Project

# Create your views here.
def main(request):
    msg_list = ["i really like buidling things", "hei stranger!"]
    msg = random.choice(msg_list)
    projects = Project.objects.all()
    return render(request, 'portfolio.html',
                    {'msg': msg,
                        'projects': projects})
