import random

tajnibroj = random.randint(1, 100)
broj_je_pogoden = False
pokusaji = 0

while not broj_je_pogoden:
    pokusaji += 1

    unos = int(input("Pogodi broj između 1 i 100: "))
    if unos < tajnibroj:
        print("Tvoj broj je manji od tajnog broja.")
    elif unos > tajnibroj:
        print("Tvoj broj je veći od tajnog broja.")
    else:
        broj_je_pogoden = True
        print(f"Bravo, pogodio si u {pokusaji} pokušaja.")
