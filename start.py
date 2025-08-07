#Modules

import sys
import time


#Variables

diplomates = int(5)
hack = int(0)
carte = int(0)
lampe = int(0)
point_risques = int(0)
name = input("Quel est votre nom ?")
ask = input("Etes-vous sur de votre séléction ?")

while ask == "non" :
     name =input("Quel est votre nom ?")
     ask = input("Etes-vous sur de votre séléction ? (Veuillez écrire oui ou non)")

else:
    print ("Bonjour " + name +".")
time.sleep(1)

avertissement = input("Attention , ce n'est pas un simple jeu , des vies dépendent de vous et de vos choix , êtes vous sur d'avoir les épaules pour ça ?")
if avertissement == "oui":
    time.sleep(2)
    print("Bien , bon courage . Vous en aurez besoin .")
    time.sleep(2)
    print("Le but du jeu est d'emmener les 5 diplomates en vie, à l'ambassade de Lisbone .")
    time.sleep(2)
    print("Pour répondre aux questions vous devez mettre la première lettre en majuscule , puis les autres en miniscules .")

    
else: 
    quit()    

time.sleep(2)
print("Nous sommes en 2042 (oui , comme dans battelfield) un conflit de ressources éclate entre le Listembourg et l'Eshil.")
time.sleep(3)
print("Dans le Listembourg , toute la population a fui vers l'Amérique, y compris le groupe de diplomate dans lequel vous êtes .")
time.sleep(3)
print("Malheuresement , votre bateau rencontre un missile eshilien , et vous faites naufrage .")
time.sleep(3)
print("Vous vous réveillez , vous et votre groupe sur une plage au Portugal , à Aveiro.")
time.sleep(3)

Evenement_1 = input("Que faire ? \n 1:Prendre des objets à l'intérieur du bateau . \n 2:Aller vers la ville \n 3:Rester camper")
if Evenement_1 =="1" :
    print("Vous retournez dans le bateau , vous arrivez dans la cabine du capitaine et vous trouvez une carte du Portugal .")
    question_1 = input("Quelle est la capitale du Portugal ?")
    
if question_1 == "Lisbonne" :
    print("Dans l'un des tiroirs , vous trouvez une carte , et une lampe torche .")   
    lampe = lampe + 1
    carte = carte + 1
    
else :
    point_risques = point_risques + 1
    print("Oh ,il semblerait que la géographie n'est pas votre point fort , dommage .")
    time.sleep(2)   
    print("Vous avez " + str(point_risques) + "point risque , dommage .")

if Evenement_1 =="2":
    print("Vous et les 5 diplomates vont au centre-ville , et vous voyez une voiture. ")
    
if Evenement_1 =="3":
    print("Vous décidez d'installer un camp car vous êtes fatigués .")            
    time.sleep(2)
    print("Un vent violent emporte les tentes.")
    time.sleep(2)
    print("Tant pis , vous dormirez à la belle étoile ce soir .")

time.sleep(3)
print("Vous allez en ville , et vous voyez un monospace , de plus , il marche ! ")

Evenement_2 = input("1: Continuer tout droit \n 2:Prendre la deuxième sortie .\n 3:Prendre à gauche .")
if Evenement_2 == "1" : 
    print(".......vous faites un détour de 50km , une carte n'aurait pas été de trop .")

if Evenement_2 == "2" :
    if carte == 1 :
        print("Eh bien ! Vous avez le sens de l'orientation .")
    else : 
        print("Vous tournez , tournez , mais en rond . Votre voiture n'a plus d'essence . Vous devez vous arreter , mais vous êtes au beau millieu de nul part .") 
        sys.exit
if Evenement_2 == "3":
    print("Vous vous retrouvez face à la plage de tout à l'heure . Oups .")    
    time.sleep("5")    
    Evenement_1 = input("Que faire ? \n 1:Prendre des objets à l'intérieur du bateau . \n 2:Aller vers la ville \n 3:Rester camper")
if Evenement_1 =="1" :
    print("Vous retournez dans le bateau , vous arrivez dans la cabine du capitaine et vous trouvez une carte du Portugal .")
    question_1 = input("Quelle est la capitale du Portugal ?")
    
if question_1 == "Lisbonne" :
    print("Dans l'un des tiroirs , vous trouvez une carte , et une lampe torche .")   
    lampe = lampe + 1
    carte = carte + 1
    
else :
    point_risques = point_risques + 1
    print("Oh ,il semblerait que la géographie n'est pas votre point fort , dommage .")
    time.sleep(2)   
    print("Vous avez " + str(point_risques) + "point risque , dommage .")

if Evenement_1 =="2":
    print("Vous et les 5 diplomates vont au centre-ville , et vous voyez une voiture. ")
    
if Evenement_1 =="3":
    print("Vous décidez d'installer un camp car vous êtes fatigués .")            
    time.sleep(2)
    print("Un vent violent emporte les tentes.")
    time.sleep(2)
    print("Tant pis , vous dormirez à la belle étoile ce soir .")        
    
Evenement_3 = input("Arrivés à Nazare , vous apercevez un homme seul sur la route , colossal , et il tient un lance-roquette pointé dans votre direction .")
print("C'est l'heure d'être un héros .\n 1:Accélerer afin de le percuter . \n 2:Faire demi-tour \n 3:S'arrêter")
  
if Evenement_3 == "1" : 
    print("Vous écrasez le champignon , mais Mister W.D appuie sur la détente . Vous et votre fine équipe n'est maintenant qu'un tas de chair et d'os... et de ferrailles aussi .")
    sys.exit 
    
if Evenement_3 =="2":
    print("Vous faites demi-tour , et vous trouvez une route alternative .")
    
if Evenement_3 =="3":
    print("Vous vous arrêtez , et Mister W.D appuie sur la détente .")
    sys.exit

print("Vous vous trouvez dans une ancienne base abandonnée . Vous entrez et tout est vide .")        
time.sleep(2)
print("Un terminal se trouve face à vous , vous ouvrez l'interface .")         
time.sleep(2)
ask_2 = input("Quelle est la cyber-attaque la plus connue ?")  

if ask_2 == "Wannacry" :
    print("Vous avez gagné le pouvoir 'hack' .")
    hack = hack + 1
else :
    print("Dommage , il s'agissait du mot de passe du terminal . Qui sait ce qu'il y avait à l'intérieur , la paix ?")
    point_risques = point_risques + 1
    if point_risques == 2 :
        print("Des câbles encombrent la pièce , l'un des diplomates marche dessus , tombe et se prend un morceau de métal rouillé dans la jugulaire . Le pauvre...")
        diplomates - 1


time.sleep(2)
print("Vous sortez du complexe avec...rien . Vous reprenez la route avec votre équipe .")
time.sleep(1)
print("En route pour Lisbonne , vous êtes sur la route lorsque vous voyez un gros SUV noir dans votre rétroviseur .")
time.sleep(2)
print("Vous voyez encore une fois cet homme collosal qui le conduit . Cette fois ci , vous ne vous en sortirez pas vivant .")
time.sleep(1.5)
print("Soit vous l'affrontrez maintenant , sois il vous handicapera plus tard .")

ask_3 = input("D'ou vient le nom de Mister W.D ? \n 1:D'une théorie d'un personnage d'Undertale .\n 2:De la langue où l'on parle avec les mains . \n 3:D'un code promo .")

if ask_3 == "1" :
    print("Bien joué !")
elif ask_3 == "2" :
    print("Dommage !")
elif ask_3 == "3" :
    print("Dommage !")
    