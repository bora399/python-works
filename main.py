import random
import time
#Taş Kağıt Makas Algoritması
# Taş > Makas / Taş < Kağıt / Kağıt > Taş / Kağıt < Makas / Makas > Kağıt / Makas < Taş 
#Taş Kağıt Makas Algoritması

#Genel Değişkenler - Sorular
isim = input("İsminiz Nedir ? ")
tur = int(input("Kaç tur oynamak istersiniz : "))
i=0
oyuncuSayi = 0
pcSayi = 0
kalanTur = 0
myList = ["Taş","Kağıt","Makas"]
#Genel Değişkenler - Sorular

#While Döngüsü
while i < tur:
    secim = input("Seçiminizi Yapınız 'Taş','Kağıt','Makas' :  ")
    secim2 = secim.capitalize()#İlk harfi büyütüyoruz, koşul ifadesi içinde yaparsak eşitliği algılamıyor
    pcSecim = random.choice(myList)
    if secim2 == pcSecim:
        print("Bilgisayar Seçimi : {}".format(pcSecim))
        time.sleep(1)#1 Saniye bekletiyor
        print("Berabere, bu el sayılmayacak !")
        print("Kalan Tur Sayısı : {}".format(tur-i))
        print()
    elif secim2 == "Taş" or secim2 == "taş" and pcSecim == "Makas":
        print("Bilgisayar Seçimi : {}".format(pcSecim))
        time.sleep(1)
        print("{} Kazandı !".format(isim))
        i+=1
        oyuncuSayi += 1
        print("Kalan Tur Sayısı : {}".format(tur-i))
        print()
    elif secim2 == "Kağıt" or secim2 == "kağıt" and pcSecim == "Taş":
        print("Bilgisayar Seçimi : {}".format(pcSecim))
        time.sleep(1)
        print("{} Kazandı !".format(isim))
        i+=1
        oyuncuSayi += 1
        print("Kalan Tur Sayısı : {}".format(tur-i))
        print()
    elif secim2 == "Makas" or secim2 == "makas" and pcSecim == "Kağıt":
        print("Bilgisayar Seçimi : {}".format(pcSecim))
        time.sleep(1)
        print("{} Kazandı !".format(isim))
        i+=1
        oyuncuSayi += 1
        print("Kalan Tur Sayısı : {}".format(tur-i))
        print()
    elif pcSecim == "Taş" and secim2 == "Makas" or secim2 == "makas":
        print("Bilgisayar Seçimi : {}".format(pcSecim))
        time.sleep(1)
        print("Bilgisayar Kazandı !")
        i+=1
        pcSayi += 1
        print("Kalan Tur Sayısı : {}".format(tur-i))
        print()
    elif pcSecim == "Kağıt" and secim2 == "Taş" or secim2 == "taş":
        print("Bilgisayar Seçimi : {}".format(pcSecim))
        time.sleep(1)
        print("Bilgisayar Kazandı !")
        i+=1
        pcSayi += 1
        print("Kalan Tur Sayısı : {}".format(tur-i))
        print()
    elif pcSecim == "Makas" and secim2 == "Kağıt" or secim2 == "kağıt":
        print("Bilgisayar Seçimi : {}".format(pcSecim))
        time.sleep(1)
        print("Bilgisayar Kazandı !")
        i+=1
        pcSayi += 1
        print("Kalan Tur Sayısı : {}".format(tur-i))
        print()
#While Döngüsü

#Sonuç Ekranı
if oyuncuSayi > pcSayi:
    print("Oyuncu Kazandı !!! Oyuncu Skor : {} /// Bilgisayar Skor : {}".format(oyuncuSayi,pcSayi))
elif pcSayi > oyuncuSayi:
    print("Bilgisayar Kazandı !!! Bilgisayar Skor : {} /// Oyuncu Skor : {}".format(pcSayi,oyuncuSayi))
elif oyuncuSayi == pcSayi:
    print("Berabere !!! Oyuncu Skor : {} /// Bilgisayar Skor : {}".format(oyuncuSayi,pcSayi))
#Sonuç Ekranı

 
    