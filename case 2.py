Bil = input("masukkan suatu bilangan : ")

try:
    bilangan = int(Bil)
    if (bilangan) > 0:
        print("positif")
    elif (bilangan) < 0:
        print("negatif")
    else:
        print("nol")
except:
    print("andah salah input bilangan")