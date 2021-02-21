#-- Final Project Recipe Application

class OrtakIsler:
    def __init__(self):
        print("\n************ Tarif olusturuludu ************")
        
    def tava(self):
        print("\nTavayi cikart ocagin altini yak")
    
    def pisir(self):
        print("Urun pisiriliyor")
        
    def firinaAt(self):
        print("Urun firina atiliyor")
        
    def hazir(self):
        print("\nUrun yenilmeyek icin hazir")
    def bekleme(self,sure):
        self.sure = sure
        print("\nUrun {} dakika sonra hazir".format(sure))
    
class Tarif1(OrtakIsler):
    def __init__(self,tarfAdi,malzeme1,malzeme2,malzeme3,malzeme4):
        self.isim = tarfAdi
        self.malz1  = malzeme1
        self.malz2 = malzeme2
        self.malz3 = malzeme3
        self.malz4 = malzeme4
        super().__init__()
        print("\nUrunuzumun adi ",self.isim)
      
    def olculer(self):
        print("\n2 bardak", self.malz1)
        print("4 bardak", self.malz2)
        print("2 tatli kasigi", self.malz3)
        print("2 yemek kasigi", self.malz4)
     
    def tarif(self):
        print("\n{} ekle sonra erit".format(self.malz4))
        print("{} ekle karistir".format(self.malz1))
        print("{}  ve {} ekle ustune kapat".format(self.malz2,self.malz3))
        
class Tarif2(OrtakIsler):
    def __init__(self,tarfAdi,malzeme1,malzeme2,malzeme3,malzeme4):
        self.isim = tarfAdi
        self.malz1  = malzeme1
        self.malz2 = malzeme2
        self.malz3 = malzeme3
        self.malz4 = malzeme4
        super().__init__()
        print("\nUrunuzumun adi ",self.isim)
    
    def olculer(self):
        print("\n1 paket", self.malz1)
        print("7 bardak", self.malz2)
        print("1 yemek kasigi", self.malz3)
        print("2 yemek kasigi", self.malz4)   

    def tarif(self):
        print("\n{} ekle ve kaynat".format(self.malz2))
        print("{} ve {} ekle ".format(self.malz1,self.malz3))
        print("{}  ekle ve karistir".format(self.malz4))            

class Tarif3(OrtakIsler):
    def __init__(self,tarfAdi,malzeme1,malzeme2,malzeme3,malzeme4):
        self.isim = tarfAdi
        self.malz1  = malzeme1
        self.malz2 = malzeme2
        self.malz3 = malzeme3
        self.malz4 = malzeme4
        super().__init__()
        print("\nUrunuzumun adi ",self.isim)
        
    def olculer(self):
        print("\n500 gram", self.malz1)
        print("1 yemek kasigi", self.malz2)
        print("1 tatli kasigi", self.malz3)
        print("1 yemek kasigi", self.malz4)

    def tarif(self):
        print("\n{} ekle sonra erit".format(self.malz4))
        print("{} ekle karistir".format(self.malz1))
        print("{}  ve {} ekle ustune kapat".format(self.malz2,self.malz3))         
                
        
obje1 = Tarif1("Pilav", "pirinc", "su", "tuz", "yag")    

obje1.olculer()
obje1.tava()
obje1.tarif()
obje1.pisir()
obje1.bekleme(15)
obje1.hazir()

obje2 = Tarif2("Makarna", "makarna", "su", "tuz", "yag")    
obje2.olculer()
obje2.tarif()
obje2.pisir()
obje1.bekleme(1)
obje2.hazir()

obje3 = Tarif3("Tavuk sote", "tavuk", "salca", "tuz", "yag")            
obje3.olculer()
obje3.tarif()
obje3.pisir()
obje1.bekleme(20)
obje3.hazir()


