import turtle
import random

def joonista_viisnurk():
    for _ in range(5):
        turtle.forward(50)
        turtle.right(72)

def joonista_ring():
    turtle.circle(25)

def joonista_ruut():
    for _ in range(4):
        turtle.forward(50)
        turtle.right(90)

def juhuslik_kujund():
    return random.choice(["viisnurk", "ring", "ruut"])

def joonista_kujund(kujund):
    turtle.penup()
    turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
    turtle.pendown()
    
    if kujund == "viisnurk":
        joonista_viisnurk()
    elif kujund == "ring":
        joonista_ring()
    elif kujund == "ruut":
        joonista_ruut()

def pea_programm():
    while True:
        turtle.clear()
        
        kujund = input("Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? ").strip().lower()
        if not kujund:
            print("Programmist väljumine...")
            break
        
        if kujund not in ["viisnurk", "ring", "ruut", "suvaline"]:
            print("Viga: Palun vali 'viisnurk', 'ring', 'ruut' või 'suvaline'.")
            continue
        
        try:
            arv = int(input("Mitu kujundit soovid joonistada? "))
            if arv <= 0:
                print("Viga: Palun sisesta positiivne arv.")
                continue
        except ValueError:
            print("Viga: Palun sisesta korrektne täisarv.")
            continue
        
        for _ in range(arv):
            valitud_kujund = kujund if kujund != "suvaline" else juhuslik_kujund()
            joonista_kujund(valitud_kujund)
        
        turtle.update()
        valik = input("Vajuta Enter, et jätkata või sisesta 'lõpeta', et väljuda.")
        if valik.lower() == 'lõpeta':
            print("Programmist väljumine...")
            break

# Käivitame programmi
pea_programm()
