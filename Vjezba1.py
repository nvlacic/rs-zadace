num1 = float(input("Unesite prvi broj:"))
num2 = float(input("Unesite drugi broj:"))
do_what = input("Unesite oznaku (+, -, * ili /) kojom želite izvršiti operaciju:")

if do_what == "+":
    result = float(num1) + float(num2)
    print ("Rezultat operacije je:" +str(result))

elif do_what =="-":
    result = float(num1) - float(num2)
    print ("Rezultat operacije je:" +str(result))

elif do_what == "*":
    result = float(num1) * float(num2)
    print ("Rezultat operacije je:" +str(result))

elif do_what == "/":
    if num2 == "0":
        print("Dijeljenje s nulom nije dozvoljeno!")
        
    else:
        result = float(num1) / float(num2)
        print ("Rezultat operacije je:" + str(result))

else:
    print ("Nepodržani operator!")