Armstorng_num = input("Armstrong olup olmadığını merak ettiğiniz sayıyı giriniz: ")
basamak_sayisi = len(Armstorng_num)
toplam = sum(int(digit) ** basamak_sayisi for digit in Armstorng_num)

if toplam == int(Armstorng_num):
    print("Evet, Bu armstrong kanki :-)")
else:
    print("Bune la :-(")
