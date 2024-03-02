import random
from django.shortcuts import render

# Create your views here.
def fortune(request):
    fortune = random.choice(fortuneList)
    context = {
        "fortune": fortune
    }
    return render(request, "randomfortune/fortune.html", context)

fortuneList = [
    "HEY, I LOVE YOU",
    "GREAT WORK FLORIDA",
    "WHAT ARE YOU UPTO",
    "CONTINUE PRACTISING"
]