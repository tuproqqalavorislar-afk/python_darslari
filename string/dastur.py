mahsulotlar = [
    'sabzi',
    'piyoz',
    'kartoshka',
    'yog',
    'olma',
    'nok',
    'olcha'
]
olindi = input('qaysi mahsulotni oldingiz:').lower()
# mahsulotlar.remove(olindi)
for i in range(len(mahsulotlar)):
    if olindi == mahsulotlar[i]:
       indeks = i
olingan = mahsulotlar.pop(indeks)
print(olingan,"mahsulot", "va qolgan mahsulot", mahsulotlar)