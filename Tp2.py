import numpy as np 

dicto=[{"nom":"Mohamed", "age":24 ,"Note":[["Math",15],["physique",20]]}]
dict1=list(dicto)

print(dict1)

#Ajouter des Etudiant avec leur nom et age et leurs notes en math et physique 

i=0
while i!=-1:
   
    i=int(input("tu veut ajouter un etudiant taper 1, Si non Taper -1 pour sortir : "))
    if i==-1:
        break
    name = str(input("donner moi le nom: "))
    age = int(input("donner moi l'age ': "))
    note_math= int(input("donner moi note de math "))
    note_physique= int(input("donner moi note de physique: "))
   
    dict1.append({"nom":name, "age":age, "Note":[["Math",note_math],["physique",note_physique]]})       
    


print(dict1)

# Convert the list of dictionaries to a NumPy array
array = np.array(dict1)

print(array)


li=[]  # list de dict pou stcoker nom etudiant avec note 

#calucul moyenne
def calcul_moyen(array):
  for i in range(len(array)):
    note_math = array[i]['Note'][0][1]
    note_physique = array[i]['Note'][1][1]
    moyenne = (note_math + note_physique) / 2
    print(f"La moyenne de {array[i]['nom']} est: {moyenne}")
    li.append({"nom":array[i]['nom'],"moyen":moyenne})
    if moyenne >16:
        print('Excelent')
    if moyenne < 16 and moyenne >= 10:
        print('Bien')   
    if moyenne < 10 :
        print('Mavais') 
        
def calcul_moyen2(array):
  for i in range(len(array)):
      note=0
      z=0
      for j in range(len(array[i])):
            note= note+array[i]['Note'][j][1]
            z=z+1
           
      moyenne = note / z
      print(f"La moyenne de {array[i]['nom']} est: {moyenne}")
      li.append({"nom":array[i]['nom'],"moyen":moyenne})
      if moyenne >16:
          print('Excelent')
      if moyenne < 16 and moyenne >= 10:
          print('Bien')   
      if moyenne < 10 :
          print('Mavais')         
        
        

#jouter une matiere 
def ajouter_matiere(array,nom):
  for i in range(len(array)):  
    new_note_francais=int(input(f"donner moi la note de {nom} pour {array[i]['nom']}: ") )
    array[i]['Note'].append([nom, new_note_francais])

# Print the updated NumPy array with the new subject
  return array


#etudiant avec moyenne plus de 12 
def etud_moy_12(li):
    for i in li:
        if (i['moyen'])>12:
            print(i['nom'])
            
            
#Retirer une matiere d'un etudiant 

def retirer_matiere(array,nom_matiere_retirer):
             
    for i in range(len(array)):
        for j in range(len(array[i]['Note'])):
            if (nom_matiere_retirer==array[i]['Note'][j][0]):
                del array[i]['Note'][j]
            break   
    return array 


#6 recherche l etudiant par son nom et afficher ses info et ses note 


def affich(arr,name):
    for i in range(len(arr)):
        if(name==arr[i]['nom']):
         print("son nom est :" , arr[i]['nom'])
         print("Age :", arr[i]['age'])
         print("Ses Notes :" )
         print("En Math = " , arr[i]['Note'][0][1])
         print("En physique = ", arr[i]['Note'][1][1])
         print("En francais = " ,arr[i]['Note'][2][1])





#7 Calculer la moyenne des matières

def moyenn_matiere(arr):
    ar = np.array(["Math","physique","francais"]) 
    not_math=0
    note_phy=0
    note_fr=0
    j=0
    for i in range(len(arr)):
        not_math=not_math+arr[i]['Note'][0][1]
        note_phy=note_phy+arr[i]['Note'][1][1]
        note_fr=note_fr+arr[i]['Note'][2][1]
        j=j+1
    
    not_math=not_math/j
    note_phy=note_phy/j
    note_fr=note_fr/j
    
    b = np.array([not_math,note_phy,note_fr])
    ar= np.stack((ar,b),axis=1)
     
    return ar    




def menu():
    print("Choisissez une option:")
    print("1. Calculer la moyenne des étudiants")
    print("2. Ajouter une matière")
    print("3. Afficher les étudiants avec plus de 12 de moyenne")
    print("4. Retirer une matière")
    print("5. Afficher un étudiant par son nom")
    print("6. Calculer la moyenne des matières")
    print("7. Calculer la moyenne apres ajouter un matierre")
    print("8. Quitter") 


    while True:     
        choix = int(input("Entrez votre choix (1-8): "))
        
        if choix == 1:
            calcul_moyen(array)
        elif choix == 2:
            nom = str(input("Donnez-moi le nom de la matière à ajouter: "))
            print(ajouter_matiere(array, nom))
        elif choix == 3:
            etud_moy_12(li)
        elif choix == 4:
            nom_matiere_retirer = str(input("Donnez-moi le nom de la matière à retirer: "))
            print(retirer_matiere(array, nom_matiere_retirer))
        elif choix == 5:
            name_etu = str(input("Donnez-moi le nom de l'étudiant à afficher: "))
            affich(array, name_etu)
        elif choix == 6:
            print(moyenn_matiere(array))
        elif choix == 7:
            print("Moyenne avec la matière ajoutée:")
            calcul_moyen2(array)    
        elif choix == 8:
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer.")
menu()      
        
        

        
        




























