# Sayılarımız için olan değişkenleri kullanıcıdan "int" yani tam sayı tipinde istiyoruz.

sayi1 = int(input("Birinci sayıyı giriniz:"))
sayi2 = int(input("İkinci sayıyı giriniz:"))

# "toplam" değişkeni, ikisinin toplamı. 
toplam = sayi1 + sayi2

# değerleri yazdıralım.
print("{0} + {1} = {2}" .format(sayi1, sayi2, toplam)) 
