#-- Hangman Game with OOP

class Hangman:
    def __init__(self,name):
        self.name = name
        self.Word = []
        self.empty = []
     
        
    def targetWord(self,word):
        self.Word = list(word)
        
        
    def play(self):
        print("\nHosgeldin",self.name)
        temp = 0
        puan = 0
        hak = len(self.Word)-2
        self.empty = list(["_" for i in range(len(self.Word))])
        while hak>0:
            charcter = input("Lutfen bir karakter giriniz :")
            if charcter in self.Word:
                index =self.Word.index(charcter)
                self.empty[index] = charcter
                temp += 1
                puan = hak*10
                print("\n")
                print(*self.empty)
                print("\ndogru harf vardir")
                
                if len(self.Word) == temp:
                    print("\nTebrikler {} {} puan ile kazandiniz".format(self.name, puan))
                    break
                
                
            
            else :
                hak -= 1 
                print(*self.empty)
                print("\n"+str(hak)+ " Hakkiniz kaldi\n")
                if hak == 0:
                    print("\nKaybettiniz\n")
                    print("Hedef kelime "+ "".join(self.Word) + "  idi")
               
            
playerName = input("Lutfen adinizi giriniz :")        
player1 = Hangman(playerName)     
player1.targetWord("globalaihub") # :)       
player1.play()
    