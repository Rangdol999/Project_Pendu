from django.http import HttpRequest
from django.shortcuts  import render
from string import ascii_uppercase
import os
import random

from numpy import append

class FilePath():
    def __init__(self, fichier):
        self.fichier = str(fichier)
    #
    def __str__(self):  
        absPath = os.path.abspath(__file__)
        pthDir1 = os.path.dirname(absPath)
        pthDir2 = os.path.dirname(pthDir1)
        fchPath = os.path.join(pthDir2,self.fichier)
        return(fchPath)


list_pendu = {
    'sport': {'FOOTBALL', 'BASKETBALL', 'SWIMMING', 'TENNISE', 'CRICKET', 'BASEBALL','BEDMENTION'},   
    'voiture': {"CADILLAC","CHEVROLET","CHRYSLER","FORD","MUSTANG","SHELBY", "LAMBORGHINI"},
    'country' : {'FRANCE', 'GERMANY', 'SPAIN', 'CHINA', 'INDIA', 'JAPAN', 'KOREA'}
    }

# HOME Page
def index(request):
  return render(request, 'index.html')

# LEVEL Page
def level(request):
  list_level = ['debutant', 'intermediarie', 'advance'
  ]
  return render(request, 'level.html', {'list_level': list_level})

# THEAM Page
def openTheam(request, id):
  list_img = ["/static/image/sport.jpeg", "/static/image/voiture.jpeg", "/static/image/country.jpeg"]
  id = {'list_pendu': list_pendu}

  return render(request, 'theam.html', {'id': id, 'list_img': list_img})

# GAME Page
def playGame(request, id, pendu_id):
  letter = []
  for c in ascii_uppercase:
    letter.append(c)

  # wordInput = input(letter)
  # print("wordInput :", awordInput)
  

  # wrongLetter = 6
  
  key, value = random.choice(list(list_pendu.items()))

  if key == pendu_id:
    print("key :", key)
    print("value :", value)
    
    a = list(value)
    b = random.choice(a)

    word_letter = []
    for word in range(len(b)):
      word_letter.append("__")
    print("word_letter :", list(word_letter))

    temp = []
    for single in b:
      # print("single :", single)
      # if single == letter:
      #   print("Hello world")
      temp.append(single)
    print("temp :", temp)
    # temp= []
    # for i in list(value):
    #   print("value :", i)
    #   temp.append(i)
    # print("temp :", temp)

    mot = []
    for one in letter:
      # print("letter One :", one)
      # print("letter :", letter)
      if one in temp:
        print("Bonjour tout le monde :", one)
      mot.append(one)

  else:
    print("hello world")
    
  return render(request, 'play.html', {'id': id, 'letter': letter} )


def myClick():
  print("Namaste")