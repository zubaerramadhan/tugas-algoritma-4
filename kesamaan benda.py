benda1 = input("Masukkan ukuran benda 1 = ")
benda2 = input("Masukkan ukuran benda 2 = ")
benda3 = input("Masukkan ukuran benda 3 = ")

try :
    benda1 = int(benda1) 
    benda2 = int(benda2)
    benda3 = int(benda3)

    if benda1 == benda2 and benda2 == benda3 :
        print("3 benda sama")
    elif benda1 == benda2 or benda1 == benda3 or benda2 == benda3 :
        print("2 benda sama")
    else :
        print("Tidak ada yang sama")

except : 
    print("angkah yang dimasukkan salah")