try: # hata yakalama yapacağım için işlem bloğuna "try" ifadesi ile başladım.
  sayi1 = int(input("Birinci sayıyı giriniz:"))
  sayi2 = int(input("İkinci sayıyı giriniz:"))
  
  # "toplam" değişkeni, ikisinin toplamı. 
  toplam = sayi1 + sayi2
  # değerleri yazdıralım.
  print("{0} + {1} = {2}" .format(sayi1, sayi2, toplam)) 
except ValueError:  # tip hataları yakalandığı zaman çalıştırılacak blok.
  print("Düzgün tipte veri girdiğinizden emin olun.")
except: # herhangi bir hata yakalandığı zaman çalıştırılacak blok.
  print("Bir sorun oluştu.")

