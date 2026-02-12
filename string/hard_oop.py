class Doktor:
    def __init__(self , name ):
        self.name = name
        self.bemorlar = []
    def add_bemor(self , bemor_name):
        self.bemorlar.append(bemor_name)
    def show_bemor(self):
        return self.bemorlar 
    def count_bemor(self):
        return len(self.bemorlar)
class Kasalxona:
    def __init__(self , name):
        self.name = name
        self.doktors = []
    def add_doctor(self , doctor_name):
        self.doktors.append(doctor_name)
    def show_doctors(self):
        for nomeri ,  doctor_ismi in enumerate(self.doktors):
            print(f"{nomeri+1}.{doctor_ismi.name} Navbat soni: {doctor_ismi.count_bemor()}")
class Bemor:
    def __init__(self , name):
        self.name = name
    def choos_doktor(self, doctor_name):
        doctor_name.add_bemor(self.name)
        print(f"{self.name} {doctor_name.name}ga navbatga yozildingiz")
        print("Navbatdagi bemorlar" , doctor_name.show_bemor())
        print("jami bemorlar soni:" , doctor_name.count_bemor())
shifohona = Kasalxona("1-Son markaziy Poliklinika")
dok1 = Doktor("Dr.Vali")
dok2 = Doktor("Dr.Ali")
shifohona.add_doctor(dok1)
shifohona.add_doctor(dok2)
bemor1 = Bemor("Valijon")
bemor2 = Bemor("Ulugbek") 
bemor3 = Bemor("Yoqubboy")
bemor1.choos_doktor(dok1)
bemor2.choos_doktor(dok2)
bemor3.choos_doktor(dok2)
shifohona.show_doctors()

