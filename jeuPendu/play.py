from tkinter import*
import random
import string

fenetre=Tk()

class jeux :

    # Constructeur
    def __init__(self):
        self.theme=""
        self.lettre=""
        self.France=["denault","ditroen","dacia","peugeot"]
        self.USA=["Cadillac","Chevrolet","Chrysler","Ford","Ford Mustang","Shelby"]
        self.erreur=0 # initalisation de l'erreur à zero
        self.mots_deja_utiliser=[] # si l'utilisateur à deja entrée une lettre ne peut le saisir de nouveau
        self.mots=[]
        self.devine=[]

     # Fin du constructeur

    def Theme(self,theme):
        self.theme=theme
        if self.theme=="France" :
            self.France=random.choice(self.France)
            self.mots=list(self.France)
            print(self.mots)

            for i in self.mots:
                self.devine.append("__")
            x= " ".join(self.devine)
            texte=Label(fenetre,text=x)
            texte.grid(row=180,column=300)
            fenetre.mainloop()
        else:
            self.USA=random.choice(self.USA)
            self.mots=list(self.USA)
            print(self.mots)

            for i in range (0,len(self.mots)):
                self.devine.append("__")
            print(f"    ".join(self.devine))

    def mots_a_devine(self,lettre): # Méthode prend en paramètre lettre
                self.lettre=lettre
                if self.lettre not in self.mots_deja_utiliser:
                     if self.lettre in self.mots: # si la lettre est dans la liste self.mots alors:
                            a=0 # en initialisé la variable à zero
                            self.mots_deja_utiliser.append(self.lettre)
                            for i in self.mots: # parcourir la liste des élements
                              if self.lettre ==i: # si la lettre saisie par l'utlisateur est égale à i alors :
                                self.devine[a]=self.lettre # on remplacer la lettre par le tire
                              a+=1
                            print(f"{self.lettre} fait bien partie du mot qu'il faut trouver")
                            texte=Label(fenetre,text=self.devine)
                            texte.grid(row=180,column=300)
                            fenetre.mainloop()
                     else: # Sinon
                        self.mots_deja_utiliser.append(self.lettre)
                        return self.erreur
                else:
                     return self.erreur

    def Gestion_des_erreurs(self,erreur):
         if self.lettre not in self.mots_deja_utiliser: # Si la lettre n'est pas dans la liste self.mots_deja_utiliserr alors:
            if self.lettre not in self.mots: # si la lettre n'est pas dans la liste self.mots alors:
                print(f"La lettre {self.lettre} ne fait pas partie du mots") # on affiche que cette lettre ne fait pas partie du mots
                self.mots_deja_utiliser.append(self.lettre) # on ajouter cette lettre dans la liste self.mots_deja_utiliser
                self.erreur+=1 # on écremnter erreur+=1
                if self.erreur ==5: # si self.erreur == 5 alors:
                        print("tu as perdu") # tu as perdu
                        fenetre.destroy() # autre méthode détruire la fenetre
                else:# Sinon
                     print(f"Il te reste {5-self.erreur} tentatives sinon tu as perdu")
            else:
                self.erreur+=1
                if self.erreur ==5:
                        print("tu as perdu")
                        fenetre.destroy() # autre méthode détruire la fenetre
                else:
                     print(f"Il te reste {5-self.erreur} tentatives sinon tu as perdu")

         else:
                print(f"Erreur cette lettre à déja etait saisie {self.mots_deja_utiliser}")
                self.erreur+=1
                if self.erreur==5:
                     print("tu as perdu")


jeux_du_pendu=jeux()

def Saisie():
    result=string.ascii_lowercase
    row=0
    column=0
    for i in result :

        bouton=Button(fenetre,text=f"{i}",command=lambda x=f"{i}": jeux_du_pendu.Gestion_des_erreurs(jeux_du_pendu.mots_a_devine(x)))
        bouton.grid(row=row,column=column)

        column+=1
        if column==10:
            row+=1
            column=0

################################################################################
##############################Choix du thème####################################
# Affichage du thème
theme_France=Label(fenetre, text="Choix du Thème",font=("Courrier",30))
theme_France.place(x=1500,y=50)

# Choix du thème France/USA
Bouton_France=Checkbutton(fenetre,text="France",height=2,width=10,font=("Courrier",20),command=lambda x="France":jeux_du_pendu.Theme(x))
Bouton_France.place(x=1490,y=100)

Bouton_USA=Checkbutton(fenetre,text="USA",height=2,width=10,font=("Courrier",20),command=lambda  x="USA":jeux_du_pendu.Theme(x))
Bouton_USA.place(x=1650,y=100)

Saisie()

fenetre.mainloop()