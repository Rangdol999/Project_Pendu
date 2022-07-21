from django.http import HttpRequest
from django.shortcuts  import render
# from string import ascii_uppercase
from string import ascii_uppercase

def index(request):
  return render(request, 'index.html')

# def show(request):
#   pass

def level(request):
  return render(request, 'level.html')

def openTheam(request, id):
  print("id :", id)
  return render(request, 'theam.html', {'id': id})

def playGame(request, id, pendu_id):
  print("id :", pendu_id, id)
  letter = []
  for c in ascii_uppercase:
    letter.append(c)
  return render(request, 'play.html', {'id': id, 'letter': letter} )