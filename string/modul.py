# def kvadrat (a):
#     b = a**2
#     return b 
# print(kvadrat(5))
# def kub (a):
#     b = a**3
#     return b
# print(kub(3))
# n = int(input('son kiriting:'))
# kopaytma = 1
# for i in range (1,n+1):
#     kopaytma = kopaytma*i 
#     print(kopaytma)


# def juft_toq_aniqla(son):
#     if son == 0:
#         return " bu son 0 ga teng"
#     elif son%2 == 0:
#         return "Bu juft son"
#     elif son < 0:
#         return "bu son manfiy"
#     else:
#         return "bu son toq"


# print(juft_toq_aniqla(2))

# def ildizni_aniqla (a):
#     b = a**1/2
#     return b 
# print(ildizni_aniqla(10))



# def ortacha_qiymat (son):
#     son = a+b
# print(ortacha_qiymat( 20 ))

# royhat = [10,20,45,23,12]
# def yigindi(royhat):
#     sum(yigindi)
#     return yigindi
# print(yigindi)

# royhat = [10,20,17,25,56,89,96]
# def kichik_son ():
#     eng_kichik = min(royhat)
#     return eng_kichik
# print(kichik_son())

# def sozlar_sonini_top (matn):
#     bolakla = matn.split()
#     uzunlik = len(bolakla)
#     return uzunlik 
# print(sozlar_sonini_top( "salom menhg dostim"))

# def harflar_sonini_top(matn):
#     uzunlik = len(matn)
#     return uzunlik
# print(harflar_sonini_top( "salom dostim"))

# def teskari_soz (matn):
#     teskari = matn [::-1]
#     return teskari
# print(teskari_soz('sevinch'))

# def bosh_harfni_top(matn):
#     bosh_harf = 0
#     for  katta_harf in matn:
#         if katta_harf.isupper ():
#             bosh_harf +=1
#     return bosh_harf
# print(bosh_harfni_top("SALOM dostim"))

# def tubligini_aniqla(son):
#     boluvchilar_soni = 0
#     for i in range (1, son+1):
#       if son%i == 0 :
#         boluvchilar_soni+=1
#     if boluvchilar_soni ==2:
#         return f"{son} tub son"
#     else:   
#         return f"{son} murakkab son"
# print(tubligini_aniqla(13))

# def tubligini_aniqla(son):
#     tublar=[]
#     murakkablar=[]
#     boluvchilar_soni = 0
#     for m in range (1, son+1):
#       for i in range(1,m+1):
#         if m%i == 0 :
#             boluvchilar_soni+=1
#         if boluvchilar_soni ==2:
#             return f"{son} tub son"
#         else:   
#             return f"{son} murakkab son"
# print(tubligini_aniqla(5))

# def katta_qilish(matn):
    # txt = matn.upper()
    # return txt 
# print(katta_qilish('salom'))

# def kichik_qilish(matn):
#     txt = matn.lower()
#     return txt 
# print(kichik_qilish('SALOM'))

# def unlilarni_yoqotish(matn):
#     unlilar = "a","e","u","i","o","A","E","U","I","O"
#     yoq_qil = matn.replase(unli,"")
#     return yoq_qil
# print(unlilarni_yoqotish('salom salom'))

# def katta_qilish(matn):
#     txt = matn.title()
#     return txt 
# print(katta_qilish('salom'))

# def palindromni_top(son):
#         if son%11==0:
#             return f"{son} bu son palindrom"
#         else:
#             return f"{son} bu son palendrom emas"
# print(palindromni_top(66))

# def palindromni_top(matn):
#     for i in matn:
#         if matn [:-1]==matn:
#             return f"{matn} bu soz palindrom"
#         else:
#             return f"{matn} bu soz palendrom emas"
        
# print(palindromni_top("ikki"))

# def ekubni_top(a,b):
#     boluvchi = []
#     eng_kichik = min(a,b)
#     for i in range(1, eng_kichik+1):
#         if a%i==0 and b%i==0:
#             boluvchi.append(i)
#         ekub = max(boluvchi)
#     return f"{a,b} sonlarning ekubi {ekub}"
# print(ekubni_top(12,16))

# def sozlar_sonini_top (matn):
#     bolakla = matn.split()
#     uzunlik = len(bolakla)
#     return uzunlik 
# print(sozlar_sonini_top( "salom mening dostim"))

# royhat=['salom','hammaga']
# def string_qilish(royhat):
#     yigish=" ".join(royhat)
#     return yigish
# print(string_qilish(royhat))

# def sonlarni_tartibla(list):
#   list.sort()
#   print(list)
# sonlar=[4,8,6,2,7,1,3,4,6,99,44,55,77]
# sonlarni_tartibla(sonlar)

# def juftlarni_yigish(son):
#     juftlar = []
#     for i in son:
#         if i%2==0:
#             juftlar.append(i)
#     return juftlar
# sonlar=[1,2,3,4,5,6,7,8,9,10,12,14,15]
# print(juftlarni_yigish(sonlar))

# def manfiylarni_yigish(son):
#     manfiy = []
#     for i in son:
#         if i<0:
#             manfiy.append(i)
#     return manfiy
# sonlar=[1,2,-3,4,5,6,-7,8,-9,10,12,-14,15]
# print(manfiylarni_yigish(sonlar))

# def darajani_hisobla(a,b):
#     daraja=a**b
#     return daraja
# print(darajani_hisobla(2,3))

# def teskari_qilish(list):
#     teskari = list [::-1]
#     return teskari
# royhat=['salom', 'hammaga']
# print(teskari_qilish(royhat))

# def kabisa_yili(yil):
#     if (yil%4==0 and yil%100!=0) or yil%400==0:
#         return f"{yil} kabisa yili"
#     else:
#         return f"{yil} kabisa yili emas"
# print(kabisa_yili(2020))    
# print(kabisa_yili(2021))
# print(kabisa_yili(2022))
# print(kabisa_yili(2023))    
# print(kabisa_yili(2024))
# print(kabisa_yili(2025))
# print(kabisa_yili(2026))
# print(kabisa_yili(2027))
# print(kabisa_yili(2028))

# def darajani_top(list):
#     darajasi=[]
#     for i in list:
#         daraja=i**2
#         darajasi.append(daraja)
#     return darajasi
# royhat=[4,5,6,]
# print(darajani_top(royhat))

# def kubni_top(list):
#     kubi=[]
#     for i in list:
#         kub=i**3
#         kubi.append(kub)
#     return kubi
# royhat=[4,3,2,]
# print(kubni_top(royhat))