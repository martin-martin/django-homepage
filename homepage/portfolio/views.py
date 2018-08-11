import random
from django.shortcuts import render

# Create your views here.
def main(request):
    msg_list = ["i really like buidling things", "hei stranger!"]
    msg = random.choice(msg_list)
    return render(request, 'portfolio.html', {'msg': msg})
