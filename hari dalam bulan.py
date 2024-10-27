bulan = int(input("Masukkan nomor bulan (1-12): "))
    
try :
    if bulan < 1 or bulan > 12:
        print("masukkan bulan 1-12")
    
    if bulan in (1,3,5,7,8,10,12):
        hari = 31
    elif bulan in (4,6,9,11):
        hari = 30
    else:
        hari = 29
    print("hari = ", hari)
except :
    print("masukkan angkah yang benar")