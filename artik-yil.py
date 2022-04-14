yil = int(input("Hangi yili kontrol etmek istiyorsun? "))

if yil % 4 ==0 :
  if yil % 100 !=0 :
    print(f"{yil} Artık Yıl ")
  else:
    if yil % 400 ==0:
      print(f"{yil}Artık Yıl ")
    else:
      print(f"{yil} Artık Yıl Değil")    
else:
  print(f"{yil} Artık Yıl Değil")     
