broj = 0
while broj < 5:
    broj +=2
print(broj)

# ispisati će se broj 6

broj = 0
while broj < 5:
    broj += 1
    print(broj)
    broj -= 1

# prikazana petlja je beskonačna zbog stalnog povećanja/smanjivanja zadanog broja koji je u ovom slučaju uvijek nula

broj = 10
while broj > 0:
    broj -= 1
    print(broj)
    if broj < 5:
        broj += 2

# petlja je beskonačna zbog uvjeta u while i if petlji