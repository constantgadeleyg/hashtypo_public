import os

import pyminizip 


# Pwogram sa ap pemet nou kripte epi kache fichye oubyen dosye ou yo


class MaskeFichye :
    
    
    
    def __init__(self) :
        self.KodSekre = ""
        self.NonDosFichPouKripte = ""
        self.NonDosKache = ""
        self.LisDosFichKripte = ""
        
# Fonksyon antre pwogram nan 
        
    def FonkByenvini(self) :
        print("Byenvini nan pwogram HASHTYPO a ! \nAk pwogram sa konfidansyalite fichye ou yo asire")
        print("Gras ak pwogram sa ou ap kapab maske fichye ou ak dosye ou genyen sou odinatè a")
        Maske.MaskDosFich()
        
        
 # Fonksyon pou kripte ak kache fichye       
    def MaskDosFich(self) :
        #self.NonDosFichPouKripte = input("\nMete non fichye oubyen dosye ou vle kripte epi kache a !\nNon Fichye ou Dosye : ")
        print("Mete non fichye a : ")
    
    
#     def MeniPrens(self):
#         Maske.FonkByenvini()
#         print("Chwazi youn nan opsyon sa yo !")
        
        
        
        
    
    
        
        
        
        
        
Maske = MaskeFichye()



AnplasmanAktyel = os.getcwd()
AnplasmanFDMaske = AnplasmanAktyel + "\\FichyeMaske\\"



try :
    Maske.LisDosFichKripte = open(AnplasmanFDMaske + "LisFichyeDatabase.txt", "r")
    Maske.LisDosFichKripte.close()
except FileNotFoundError:
    try:
        os.makedirs(AnplasmanFDMaske)
    except FileExistsError:
        os.makedirs(AnplasmanFDMaske)
    Maske.LisDosFichKripte = open (AnplasmanFDMaske + "LisFichyeDatabase.txt","a")
    Maske.LisDosFichKripte.write("Bonjou")
    Maske.LisDosFichKripte.close()



#print(AnplasmanAktyel)

Maske.FonkByenvini()

    
        