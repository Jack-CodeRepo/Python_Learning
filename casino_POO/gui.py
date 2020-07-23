import tkinter as tk
import fonctions.casino_fonctions

# ==================================================================================================
#   Variables
# ==================================================================================================


# ==================================================================================================
#   Fonctions
# ==================================================================================================

def resize():
    width = width_entry.get()
    height = height_entry.get()
    window.geometry(f"{width}x{height}")


def test_output():
    test = "Salut! Ca va ?"
    frame_output.insert(tk.END, test)


# ==================================================================================================
#   initialisation de la fenetre
# ==================================================================================================

window = tk.Tk()
window.title("Casino")
# window.geometry(f"{width}x{height}")
# window.geometry(str(width)+'x'+str(height))
# window.geometry("{width}x{height}".format(width=width, height=height))
# window.geometry("%ix%i" %(width, height))

window.iconbitmap("img/dice.ico")
window.config(background="#16A04E")

# ==================================================================================================
#   Frame
# ==================================================================================================

frame = tk.Frame(window, bg="#16A04E")
frame_output = tk.Text(frame, font=("Calibri", 20), bg="#16A04E", fg='white')
frame_output.pack(expand='True')


# ==================================================================================================
#   Redimmensionner la fenetre
# ==================================================================================================

width_label = tk.Label(window, text="Largeur")
width_label.pack()
width_entry = tk.Entry(window)
width_entry.pack()


height_label = tk.Label(window, text="Hauteur")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

# ==================================================================================================
#   Menu
# ==================================================================================================

menu_bar = tk.Menu(window)

menu_file = tk.Menu(menu_bar, tearoff=0)
menu_file.add_command(label="Nouveau", command=test_output)
menu_file.add_command(label="Quitter", command=window.quit)
menu_file.add_command(label="Changer resolution", command=resize)

menu_bar.add_cascade(menu=menu_file, label="Acceuil")




# ==================================================================================================
#   Configuration de window / fenetre principale
# ==================================================================================================
window.config(menu=menu_bar)




# ==================================================================================================
#   Affichage
# ==================================================================================================
frame.pack(expand = 'True')

window.mainloop()