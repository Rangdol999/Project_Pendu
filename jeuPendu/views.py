from django.http import HttpRequest
from django.shortcuts  import render
# from string import ascii_uppercase
from string import ascii_uppercase
import random

list_pendu = {
    'sport': {'Football', 'basketball', 'swimming', 'tennise', 'cricket', 'baseball','bedmention'},   
    'voiture': {"Cadillac","Chevrolet","Chrysler","Ford","Ford Mustang","Shelby", "lamborghini"},
    'country' : {'france', 'germany', 'spain', 'china', 'india', 'japan', 'korea'}
    }

def index(request):
  return render(request, 'index.html')

# def show(request):
#   pass

def level(request):
  list_level = ['debutant', 'intermediarie', 'advance'
  ]
  return render(request, 'level.html', {'list_level': list_level})

def openTheam(request, id):
  list_img = ["/static/image/sport.jpeg", "/static/image/voiture.jpeg", "/static/image/country.jpeg"]
  id = {'list_pendu': list_pendu}

  return render(request, 'theam.html', {'id': id, 'list_img': list_img})

def playGame(request, id, pendu_id):
  print("id :", pendu_id, id)

  # list_word = []

  word = random.choice(pendu_id)
  print("word :", word)
  # for i in word:
  #   print("i :", i)

  letter = []
  for c in ascii_uppercase:
    letter.append(c)
  return render(request, 'play.html', {'id': id, 'letter': letter} )