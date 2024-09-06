from tkinter import *
import math
import tkinter as tk

def calcolatrice_grafica():
    # Funzione per aggiornare il display
    def aggiorna_display(testo):
        display.delete(0, tk.END)
        display.insert(0, testo)

    def clicca(tasto):
        corrente = display.get()
        aggiorna_display(corrente + str(tasto))

    def esegui_operazione():
        try:
            espressione = display.get()
            if 'sqrt' in espressione:
                numero = float(espressione.split('sqrt')[1])
                risultato = math.sqrt(numero)
            else:
                risultato = eval(espressione)
            aggiorna_display(str(risultato))
        except Exception:
            aggiorna_display("operazione non eseguibile")

    def cancella():
        aggiorna_display("")  # Pulisce il display

    # Creazione della finestra principale
    root = tk.Tk()
    root.title("Calcolatrice")
    colore_sfondo_pulsante = "blue"
    colore_testo_pulsante = "red"
    colore_sfondo_display = "black"
    colore_testo_display = "white"

    # Creazione dello schermo digitale
    display = tk.Entry(root, width=25, font=("Arial", 18), borderwidth=2, relief="solid",
                      bg=colore_sfondo_display, fg=colore_testo_display)
    display.grid(row=0, column=0, columnspan=4)
   
    display.grid(row=0, column=0, columnspan=4)

    pulsanti = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('^', 5, 0), ('C', 5, 1)
    ]

    for (testo, riga, colonna) in pulsanti:
        if testo == '=':
            tk.Button(root, text=testo, width=5, height=2, font=("Arial", 18),
                    command=esegui_operazione).grid(row=riga, column=colonna)
        elif testo == 'C':
            tk.Button(root, text=testo, width=5, height=2, font=("Arial", 18),
                     command=cancella).grid(row=riga, column=colonna)
        elif testo == '^':
            tk.Button(root, text=testo, width=5, height=2, font=("Arial", 18),
                      command=lambda: clicca('**')).grid(row=riga, column=colonna)
        else:
            tk.Button(root, text=testo, width=5, height=2, font=("Arial", 18),
                      command=lambda t=testo: clicca(t)).grid(row=riga, column=colonna)

    root.mainloop()

if __name__ == "__main__":
    calcolatrice_grafica()

