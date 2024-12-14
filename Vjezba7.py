def znak(lozinka):
    return any(i.isdigit() for i in lozinka)

def rijec(rijec, lozinka):
    return rijec.lower() in lozinka.lower ()



def provjera (lozinka):
    if len(lozinka) not in range (8, 15):
        return "Lozinka mora sadržavati između 8 i 15 znakova."
    
    if lozinka==lozinka.lower() or znak(lozinka)==False:
        return "Lozinka mora sadržavati barem jedno veliko slovo i jedan broj."
    
    if rijec ("password", lozinka) or rijec ("lozinka", lozinka):
        return "Lozinka ne smije sadržavati riječ password ili lozinka."
    return "Lozinka je jaka!"

lozinka=input("Unesite lozinku: ")
print(provjera(lozinka))