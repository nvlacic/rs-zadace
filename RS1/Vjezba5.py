broj = int(input("Unesite broj za izračun faktorijela: "))

faktorijel = 1
for i in range(1, broj+1):
    faktorijel *=i
print(f"Faktorijel u for petlji je: {faktorijel}")


faktorijel = 1
while broj>0:
    faktorijel *=broj
    broj-=1
print(f"Faktorijel u while petlji je: {faktorijel}")