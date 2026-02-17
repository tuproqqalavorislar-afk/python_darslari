# 1
# class Avto:
#     def __init__(self, model, rang , yurgan , yil, uzatma ):
#         self.model = modeli
#         self.rang = rangi
#         self.yurgani = yurgani 
#         self.yil = yili
#         self.uzatma = uzatma

#     def get_info(self):
#         return f"{self.model} mashina haqida ma'lumotlar"
# class Mersedes(Avto):
#     def __init__(self, model, rang, yurgan, yil, uzatma,class_turi, salon, amg):
#         super().__init__(madel, rang, yurgan, yil, uzatma)
#         self.class_turi = class_turi
#         self.salon = salon
#         self.amg = amg
#     def sport_rejimi(self):
#         if self.amg:
#             return "AMG Turbo rejim yoqildi"
#         else:
#             return "Bu Mers AMG emas" 


# 2
# class Ota:
#     def __init__(self, ism, yosh):
#         self.ism = ismi
#         self.yosh = yoshi

#     def get_info(self):
#         return f"{self.ism} ismi: yoshi:"

# class Bola(Ota):
#     def __init__(self, ism, yosh, maktab_nomi):
#         super().__init__(ism, yosh)
#         self.school = maktab_nomi
#     def get_data(self):
#         return f"{self.get_info()}\nMaktab nomi: {self.school}"
# bola = Bola("Sevinch",13,"6-maktab")         


# 3
# class Hayvon:
#     def __init__(self,nomi,jinsi,rangi):
#         self.nomi = nomi
#         self.jinsi = jinsi
#         self.rangi = rangi
#     def get_info(self):
#         return f"Nomi: {self.nomi}\nJinsi: {self.jinsi}\nRangi: {self.rangi}"
# class It(Hayvon):
#     def __init__(self, nomi, jinsi, rangi,turi,urug):
#         super().__init__(nomi, jinsi, rangi)
#         self.turi = turi
#         self.urug = urug
#     def get_data(self):
#         return f"{self.get_info()}\nTuri: {self.turi}\nUrug'i: {self}"
# class Mushuk(Hayvon):
#     def __init__(self, nomi, jinsi, rangi, turi):
#         super().__init__(nomi, jinsi, rangi)
#         self.turi = turi
#     def get_data(self):
#         return f"Turi: {self.turi}" 



# 4
# class Avto:
#     def __init__(self,madel,yil,rang,dvigatel,yoqilgi,uzatma):
#         self.madel = madel
#         self.yil = yil
#         self.rang = rang
#         self.dvigatel = dvigatel
#         self.yoqilgi = yoqilgi
#         self.uzatma =uzatma
#     def get_info(self):
#         return f"{self.madel} mashinasi haqida ma'lumotlar:\n"
# class Avtomobil(Avto):
#     def __init__(self, madel, yil, rang, dvigatel, yoqilgi, uzatma):
#         super().__init__(madel, yil, rang, dvigatel, yoqilgi, uzatma)
#     def get_info(self):
#         return f"{self.get_info()}Yili: {self.yil}\nRang: {self.rang}\nDvigatel: {self.dvigatel}\nYoqilgi: {self.yoqilgi}\nUzatma: {self.uzatma}"
# 5
# class Talaba:
#     def __init__(self,yoshi,ismi):
#         self.yoshi = yoshi
#         self.ismi = ismi
#     def get_info(self):
#         return f"Ismi: {self.ismi}\nYoshi: {self.yoshi}"
# class Bakalavr(Talaba):
#     def __init__(self, yoshi, ismi,maktab_baholari):
#         super().__init__(yoshi, ismi)
#         self.baho = maktab_baholari
#     def get_data(self):
#         return f"{self.get_info()}\nMaktab baholari: {self.baho}"
# class Magistr(Talaba):
#     def __init__(self, yoshi, ismi,bakalavr_bahosi):
#         super().__init__(yoshi, ismi)
#         self.bakalavr = bakalavr_bahosi
#     def get_data(self):
#         return f"{self.get_info()}\n Bakalavr bahosi: {self.bakalavr}"


# 6
# class Ustoz:
#     def __init__(self,ismi,yoshi,fani):
#         self.ismi = ismi
#         self.yoshi = yoshi
#         self.fan = fani
#     def get_info(self):
#         return f"Ismi: {self.ismi}\nYoshi: {self.yoshi}\nDars beradigan fani: {self.fan}"
# class InformatikaUstozi(Ustoz):
#     def __init__(self, ismi, yoshi, fani, dasturlash_tili,project):
#         super().__init__(ismi, yoshi, fani)
#         self.til = dasturlash_tili
#         self.project = project
#     def get_data(self):
#         return f"{self.get_info()}\nBiladigan dasturlsh tillari: {self.til}\nIshtirok etgan va amalga oshirgan loyihalari: {self.project}"



# 7
# class Tech:
#      def __init__(self, rangi, model):
#          self.rang = rangi
#          self.model = model
#      def get_tech(self):
#          return f"Modeli: {self.model}\nRangi: {self.rang}"
# class Kompyuter(Tech):
#      def __init__(self, model, rangi,xotirasi,ram):
#          super().__init__(model, rangi)
#          self.memory = xotirasi
#          self.ram = ram
#      def kompyuter_data(self):
# 8
# class Kompyuter:
#     def __init__(self, nomi, ekran ):
#         self.name = nomi
#         self.screen = ekran

#     def info(self):
#         return f"Kompyuter nomi {self.name}\nKompyuter ekrani o'lchami:{self.screen}"

# class Noutbook(Kompyuter):
#     def __init__(self, nomi, ekran, shlef, touchbat, akkumlyator):
#         super().__init__(nomi, ekran)
#         self.shelf = shelf 
#         self.touchbat = touchbat
#         self.batareya = akkumlyator

#     def get_info(self):
#         return f"{self.info()}\nNoutbook ochilish gradusi {self.shlef}\nTouchbat borligi :{self.touch}\nZaryadkasi :{self.batareya}"


# hp = Noutbook("Hp Envy" , "15.6 dyumm" , "180^gradus" , "Bor" , "aktiv holatda 5 soatga yetadi")

# print(hp.get_info())


# 9
# class Shaxs:
#     def __init__(self,ismi,yoshi,birth_day):
#         self.ismi = ismi
#         self.yoshi = yoshi
#         self.birthday = birth_day
#     def shaxs_info(self):
#         return f"Ismi: {self.ismi}\nYoshi: {self.yoshi}\nTug'ilgan kuni: {self.birthday}"
# class Oqituvchi(Shaxs):
#     def __init__(self, ismi, yoshi, birth_day,fani):
#         super().__init_-(ismi, yoshi, birth_day)
#         self.fan = fani
#     def get_teacher(self):
#         return f"{self.get_info()}\nDars beradigan fani: {self.fan}"

# 10
# class Mashina:
#     def __init__(self , rusumi , yil , rangi):
#         self.model = rusumi
#         self.year = yil
#         self.color = rangi
#     def get_info(self):
#         return f"Mashina rusumi:{self.model}\nMashina yili:{self.year}\nMashina rangi:{self.color}"
# class Yuk_mashina(Mashina):
#     def __init__(self, rusumi, yil, rangi , yuk):
#         super().__init__(rusumi, yil, rangi)
#         self.yuk = yuk
#     def get_info(self):
#         return f"{self.get_info()}\n yuk:"
# mashin = Yuk_mashina("fura","2023","oq" ,"shassi")
# print(mashin.get_info())
# 11
# class Uchuvchi:
#     def __init__(self , ismi , yoshi, samolyot_turi ):
#         self.name = ismi
#         self.age = yoshi
#         self.plane = samolyot_turi
#     def get_info(self):
#         return f"Uchuvchining ismi:{self.name}\nUchuvchining yoshi:{self.age}\nUchuvchi boshqaradigan samolyot turi:{self.plane}"
# class Harbiy_uchuvchi(Uchuvchi):
#     def __init__(self, ismi, yoshi, samolyot_turi, quroli_kuch):
#         super().__init__(ismi, yoshi, samolyot_turi)    
#         self.armed_forces = quroli_kuch
#     def info(self):
#         return f"{self.get_info()}\nQurolli kuch turi:{self.armed_forces}"
# uchuvchi=Harbiy_uchuvchi("Olim",25,"MiG","qiruvchi")    
# print(uchuvchi.info())
# 12
# class Kitob:
#     def __init__(self , nomi , turi):
#         self.name = nomi
#         self.type = turi
#     def get_info(self):
#         return f"kitobning nomi:{self.name}\nkitobning turi:{self.type}"
# class Darslik(Kitob):
#     def __init__(self, nomi, turi , maxsus_oqish_uchun , tartiblangan_mavzular):
#         super().__init__(nomi, turi)
#         self.special = maxsus_oqish_uchun
#         self.organized_topics = tartiblangan_mavzular
#     def info(self):
        # return f"{self.get_info()}\nMaxsus oqish uchun:{self.special}\nTartiblangan mavzu:{self.organized_topics} "
# kitob1 = Darslik("informatika","dasturlash haqida","majburiy oqish","tartiblangan mazular")
# print(kitob1.info())
# 13# 
# class Hayvon:
#     def ovoz(self):
#         return ("hayvonlar har hil ovoz chiqaradi")
# class Mushuk(Hayvon):
#     def __init__ (self,mushuk):
#         self.cat = mushuk
#     def info(self):
#         return f"mushukning ovozi:{self.ovoz}"
# cat1 = Mushuk("Miyov-Miyov")
# print(cat1.info)
# # 14
# class Qurilma:
#     def __init__(self , nomi , turi , narxi):
#         self.type = turi
#         self.price = narxi
#         self.name = nomi
#     def get_info(self):
#         return f"Qurilma nomi:{self.name}\nQurilma turi:{self.type}\nQurilma narxi:{self.price} "
# class Telefon(Qurilma):
#     def __init__(self , nomi , turi , narxi , sensor , ekran_hajmi):
#         super().__init__(nomi , turi , narxi)    
#         self.fingerprint = sensor
#         self.size = ekran_hajmi
#     def info1(self):
#         return f"{self.get_info()}\nKirish usuli:{self.fingerprint}\nEkran hajmi:{self.size}"
# class Noutbook(Qurilma):
#     def __init__(self , nomi , turi , narxi , shelf , touchbat , akkaumlyator ):
#         super().__init__(nomi , turi , narxi)
#         self.shelf = shelf
#         self.touchbat = touchbat
#         self.batareya = akkaumlyator
#     def info2(self):
#         return f"{self.get_info()}\nNoutbook ochilish gradusi {self.shelf}\nTouchbat borligi :{self.touchbat}\nZaryadkasi :{self.batareya}"
# phone = Telefon("VIVO","telefon","7000000","sensor(barmoq bilan)","kichik ekran")
# hp = Noutbook("Hp Envy" , "kompyuter" ,"8000000"  , "180^gradus" , "Bor" , "aktiv holatda 5 soatga yetadi")
# print(phone.info1())
# print(hp.info2())
# 15
class Kampaniya:
    def __init__(self , nomi , foyda_olish , hamkorlik):
        self.name = nomi
        self.to_make_pofit = foyda_olish
        self.cooperation = hamkorlik
    def get_info(self):
        return f"Kompaniya nomi:{self.name}\nFoyda olish:{self.to_make_pofit}\nHamkorlik:{self.cooperation}"
class Ishchi(Kampaniya):
    def __init__(self, nomi, foyda_olish, hamkorlik , ismi , familya , yoshi , malakasi):
        super().__init__(nomi, foyda_olish, hamkorlik)
        self.name1 = ismi
        self.surname = familya
        self.age = yoshi
        self.qualification = malakasi
    def info(self):
        return f"{self.get_info()}\nIshchining ismi:{self.name1}\nFamilyasi:{self.surname}\nIshchining yoshi:{self.age}\nMalakasi:{self.qualification}"
ishchi = Ishchi("NBU","5mlnda boshlanadi","bor","Ali","Alixonov",25,"5 yil")
print(ishchi.info())