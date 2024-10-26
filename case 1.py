SuhuTubuh = input("masukkan suhu tubuh anda: ")

try:
    suhu = int(SuhuTubuh)
    if suhu >= 38:
        print("anda demam")
    else:
        print("anda tidak demam")
except:
    print("anda salah input")