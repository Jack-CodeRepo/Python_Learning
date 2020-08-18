import string
import tkinter as tk
import random

# fonction pour générer le mot de passe
def generate_password():
    minLength=6
    maxLength=24
    all_char= string.ascii_letters + string.punctuation + string.digits

    password = "".join(random.choice(all_char) for i in range(random.randint(minLength, maxLength)))

    # on vide passwd_input
    passwd_input.delete(0, 'end')
    # puis on l'alimente avec le contenu de la variable password
    passwd_input.insert(0, password)




#fonction qui donne le meme resultat que generate_password()
def generate_password_alt():
    minLength=6
    maxLength=24
    password = ""
    passwordList = []
    all_char= string.ascii_letters + string.punctuation + string.digits
    for x in range(random.randint(minLength, maxLength)):
        passwordList.append(str(random.choice(all_char)))
        x+=0    # le non usage de la variable 'x' renvois un warning dans l'IDE
    password = password.join(passwordList)
    print(password)

    # on vide passwd_input
    passwd_input.delete(0, 'end')
    # puis on l'alimente avec le contenu de la variable password
    passwd_input.insert(0, password)







window = tk.Tk()
window.title("Password Generator")
window.geometry("720x480")
window.iconbitmap("img/key.ico")
window.config(background='#4065a4')

# creation de la frame
frame = tk.Frame(window, bg='#4065a4')

# sub box right side of screen
boiteADroite = tk.Frame(frame, bg='#4065a4')
# titre
titre = tk.Label(boiteADroite, text="Password Generator", font=("Helvetica", 20), bg='#4065a4', fg="white")
titre.pack()
# champ/entree/input/saisie
passwd_input = tk.Entry(boiteADroite, font=("Helvetica", 20), bg='#4065a4', fg="white")
passwd_input.pack(fill="x")

# place boiteADroite à droite de la main frame
boiteADroite.grid(row=0, column=1, sticky="w")

# menu barre
menu_bar = tk.Menu(window)
#sous menu
menu_file = tk.Menu(menu_bar, tearoff=0)
menu_file.add_command(label="Nouveau password", command=generate_password)
menu_file.add_command(label="Nouveau password alternatif", command=generate_password_alt)

menu_file.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Main", menu=menu_file)



#configurer la fenetre pou ajouter menu_bar
window.config(menu=menu_bar)


frame.pack()

# affichage
window.mainloop()