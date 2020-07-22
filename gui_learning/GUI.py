import tkinter as tk
import webbrowser as WB

# fonction pour ouvrir un lien vers youtube
def open_youtube():
    WB.open_new("https://www.youtube.com/")



# objet de la fenetre
fenetre = tk.Tk()

# titre de la fenetre
fenetre.title("Casino")

# resolution minimale
fenetre.minsize(640,360)

#resolution
fenetre.geometry("1080x720")

# icone de la fenetre en haut à gauche
fenetre.iconbitmap("img/dice.ico")

# couleur de fond de la fenetre
fenetre.config(background='#18985D')

# creer une frame / espace dans la fenetre
frame = tk.Frame(fenetre, bg='#18985D', bd = 1, relief = 'sunken')

# ajouter du texte
# la variable fenetre_titre contient la generation du texte et son emplacement, ici dans la frame
fenetre_titre = tk.Label(frame, text="Bienvenue au casino!", font=("Calibri", 30), bg='#18985D', fg='white')
# afficher le texte avec .pack()
fenetre_titre.pack()

# on genere un autre texte, affilié à la fenetre principale et non pas à la frame
fenetre_sousTitre = tk.Label(fenetre, text="Vive l'argent", font=("Calibri", 10), bg='#18985D', fg='white')
fenetre_sousTitre.pack()

# on affiche la frame et ses composants
frame.pack(expand = 'True')

# les boutons
button = tk.Button(frame, text="Lien vers Youtube", font=("Calibri", 10), bg='#E31515', fg='white', command=open_youtube)
button.pack(pady='50', fill='x')

fenetre.mainloop()