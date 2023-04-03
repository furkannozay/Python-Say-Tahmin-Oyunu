import random
random.seed()   #Prepare random number generator

tutulanSayi = int(random.random() * 50)
tahminSayisi = 5
while True:    #This simulates a Do Loop
    print("bir tahmin giriniz")
    girilenSayi = int(input())
    if girilenSayi == tutulanSayi:
        print("Tebrikler bildiniz" + str(tutulanSayi))
    else:
        if girilenSayi < tutulanSayi:
            print("Daha büyük bir sayı girin")
        else:
            print("Daha küçük bir sayı girin")
    tahminSayisi = tahminSayisi - 1
    if not(tahminSayisi > 0): break   #Exit loop
print("Tahmin hakkınız kalmadı :(")
