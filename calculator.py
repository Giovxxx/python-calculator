from math import sqrt
import time 
import tkinter as tk
messaggio_benvenuto=f""" Benvenuto nel programma Calcolatrice
--- Scrivi 1 se vuoi effettuare una somma ---
--- Scrivi 2 se vuoi effettuare una sottrazione ---
--- Scrivi 3 se vuoi effettuare una moltiplicazione ---
--- Scrivi 4 se vuoi effettuare una Divisione ---
--- Scrivi 5 se vuoi effettuare un calcolo esponenziale ---
--- Scrivi 6 se vuoi effettuare una radice quadrata ---
- se vuoi uscire dal programma digita ESC -
"""
messaggio_continuo = ("Apprezziamo molto il tuo gesto")
messaggio_arrivederci = ("Grazie per aver usato il programma")
lettere_ok = ['Si','SI','si','sI','no','NO','No','nO']
ultime_lettere = lettere_ok[-4:]
prime_lettere = lettere_ok[:4]
while True:
    print(messaggio_benvenuto)
    scelta = input("scegli un operazione:  ")

    print(scelta)

    if scelta == "1":
        print("Hai scelto addizione")
        time.sleep(3.0)   
        a = float(input("Scegli il primo numero da sommare: "))
        b = float(input("Scegli il secondo numero: "))
        print("Il risultato dell'addizione corrisponde a ", str(a + b))

    elif scelta == "2":
        print("Hai scelto sottrazione")
        time.sleep(3.0)   
        a = float(input("Scegli il primo numero da sottrarre: "))
        b = float(input("Scegli il secondo numero: "))
        print("Il risultato della sottrazione corrisponde a ", str(a - b)) 

    elif scelta == "3":
        print("Hai scelto moltiplicazione")
        time.sleep(3.0)   
        a = float(input("Scegli il primo numero da moltiplicare: "))
        b = float(input("Scegli il secondo numero: "))
        print("Il risultato della moltiplicazione corrisponde a ", str(a * b))   


    elif scelta == "4":
        print("Hai scelto divisione")
        time.sleep(3.0)   
        a = float(input("Scegli il numeratore: "))
        b = float(input("Scegli il denominatore: "))
        print("Il risultato della divisione  corrisponde a ", str(a / b))  

    elif scelta == "5":
        print("Hai scelto calcolo esponenziale")
        time.sleep(3.0)   
        a = float(input("Scegli il primo numero: "))
        b = float(input("Scegli il secondo numero: "))
        print("Il risultato del calcolo esponenziale corrisponde a ", str(a ** b))   

    elif scelta == "6":
        print("Hai scelto radice quadrata")
        time.sleep(3.0)   
        a = float(input("Scegli il  numero: "))
        
        print("Il risultato della radice corrisponde a ", str(sqrt(a)))
    else:
        print("mi dispiace calcolo non trovato ")
        continue
    fare_dopo = "Vuoi continuare?"
    time.sleep(1.5)
    fare_dopo2 = input("Se vuoi continuare digita Y/y,\nse vuoi smettere digita N/n: ")
    time.sleep(1.7)
    if fare_dopo2 in ("Y", "y"):
        time.sleep(1.0)
        print(messaggio_continuo)
        time.sleep(2.0)
        continue
    elif fare_dopo2 in ("N", "n"):
        print(messaggio_arrivederci)
        time.sleep(2.0)
        break
    else:
        time.sleep(2.5)
       
        print("risposta non valida")

        time.sleep(1.0)
        risposta_utente=str(input("fornisci una risposta valida digitando Si/SI si/sI o No/No nO/no:   \n "))
        if risposta_utente in prime_lettere:
             time.sleep(2.0)
             print("ora tornerai al menù principale")
             continue
        elif risposta_utente in ultime_lettere:
             time.sleep(2.0)
             print("grazie per essere stato qui")
             break
        else:
            print("fornisci una risposta valida")

 
    
