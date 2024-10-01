
#grunden

import requests
import json
import sys
 
class elever:
    def __init__(self, name: str, lastname: str, email:str, phone:str ): 
        self.name = name
        self.lastname = lastname
        self.email = email
        self.phone = phone
    def prLista():
        for elev in EleverlistaUP:
            print(f'Elevnamn: {elev.name}')

class Lärare:
    def __init__(self, Lärarnamn: str='edvin' , Lösenord: str='123' )->None:
        self.Lärarnamn = Lärarnamn
        self.Lösenord = Lösenord



    def inlogg(self)->str:
        while True:
            AngeAnvändarnamn=input('Namn: ').lower()
            AngeLösenord=input('Lösenord: ')
            if AngeAnvändarnamn == self.Lärarnamn and AngeLösenord == self.Lösenord :
                print('Välkommen lärare Edvin')
                break
            else:
                print('Inloggning misslyckad, försök igen')


        
ExternData = requests.get("https://dummyjson.com/users")

InternData = ExternData.text

PythonData = json.loads(InternData)

EleverlistaUP = []

for delar in PythonData["users"]:
    HittaElever: elever = elever(
        name=delar["firstName"], 
        lastname=delar["lastName"], 
        email=delar["email"],
        phone=delar["phone"]
    )
    EleverlistaUP.append(HittaElever)




#----------------------------------------------------------------------------------------------------------------------------------------------
# Här är alla defs som kommer bygga up programmet




def Menynbeskrivning()-> str:
    print('\n Klass lista: 1 \n Sök elev: 2 \n Logga ut: 3 \n')




def HämtaUtListan()-> str:
    for elev in EleverlistaUP:
        print(f'Elevnamn: {elev.name} {elev.lastname} , Mail: {elev.email} , Telefon: {elev.phone} ')
        print('Återvänder till menyn')
    

def HämtaUtElev()-> str:
    search_HittaElever = input('Vem vill du söka efter :')
    for HittaElever in EleverlistaUP:
        if HittaElever.name.lower() == search_HittaElever.lower():
            print(f'Fullständingt namn: {HittaElever.name} {HittaElever.lastname}')
            print(f'Mail: {HittaElever.email}')
            print(f'Telefon: {HittaElever.phone}')
            break
    else:
        print('ingen elev hittad')
        
            

def KräverLoopPåHämtaUtElev()->None:
    HämtaUtElev()
    while True:
        ForsättMedMinJävlaLoop=input('Vill du kolla upp en annan elev? svara ja eller nej : ').lower()
        if ForsättMedMinJävlaLoop=='ja':
            HämtaUtElev()
            continue
        if ForsättMedMinJävlaLoop=='nej':
            break
        else:
            print('Felaktig inmatning, Frågar igen! ')
            continue
    

            


#----------------------------------------------------------------------------------------------------------------------------------------------
#Här är programmet byggt med hjälp av alla defs och bästmeda variabler

Edvin_Lärare: Lärare= Lärare()
Edvin_Lärare.inlogg()
while True:
    Menynbeskrivning()
    Lärar_Val: str=input('Vad vill du göra? : ')
    while True:
        if Lärar_Val == '1':
            while True:
                HämtaUtListan()
                break
            break
        if Lärar_Val =='2':
            while True:
                KräverLoopPåHämtaUtElev()
                break
            break
        if Lärar_Val=='3':
            print('loggar ut')
            sys.exit()
        else: 
            print('Felaktig inmatning, återvänder till menyn')
            break

    
#----------------------------------------------------------------------------------------------------------------------------------------------

                

# while True:
#     print("""          Lista = 1
#           Sök elev = 2 
#           Logga ut = 3""")
#     Lärar_Val=input('Vad vill du göra? : ')
#     while True:
#         if Lärar_Val=='1':
#             for elev in EleverlistaUP:
#                 print(f'Elevnamn: {elev.name} {elev.lastname} , Mail: {elev.email} , Telefon: {elev.phone} ')
#             break
#         if Lärar_Val=='2':
#             search_HittaElever = input('Vem vill du söka efter ?\n')
#             for HittaElever in EleverlistaUP:
#                 if HittaElever.name.lower() == search_HittaElever.lower():
#                     print(HittaElever.name, HittaElever.lastname)
#                     print(HittaElever.email)
#                     print(f'Telefon: {HittaElever.phone}')
#                     break
#                 else: 
#                     print('Personen finns inte')
#                     break
#             break
#         if Lärar_Val=='3':
#             break
#     Stäng=input('vill du stänga programmet: ').lower()
#     if Stäng== 'ja':
#         break
#     elif Stäng== 'nej':
#         continue
#     else:
#         print('Felaktig inmatning, återvänder till menyn')

        

#gör en while true loop
#Full lista med all info = 1
#Välj elev->välj info från lista


#MAIN Branch
# import requests
# import json
# import re


# Name_Pattern =re.compile(r'\"firstName\"\:\s\"[A-Z,a-z]+\"')
# name_P2 = re.compile(r'[A-Z,a-z]+')
# Found_Name_Pattern=Name_Pattern.finditer()



# Dummy_Import = requests.get('https://dummyjson.com/users')
# Dummy_Data: dict = Dummy_Import.json()

# print(Dummy_Data)

# # Chosen_Data: dict = json.loads(Dummy_Data)


#Skippa denna del


#Shilans kod

# import requests
# import json

# class Person:
#     def __init__(self, name: str , lastname: str, email: str, phone: str): #varför behövs allt annat en self?
#         self.name = name
#         self.lastname = lastname
#         self.email = email
#         self.phone = phone

        




# response = requests.get("https://dummyjson.com/users")


# data = response.text

# json_data = json.loads(data)

# persons = []


# for user in json_data["users"]:
#     person = Person(
#         name=user["firstName"], 
#         lastname=user["lastName"], 
#         email=user["email"],
#         phone=user["phone"]
#         )
#     persons.append(person)





#byggd med hjälp av shilans kod, har försökt att förtydliga vissa saker men varierande variabelnamn, byggt upp en inloggning, skapat en lista med namn mail och telefonnummer
# import requests
# import json

 
# class elever:
#     def __init__(self, name, lastname, email, phone ): #varför behövs allt annat en self?
#         self.name = name
#         self.lastname = lastname
#         self.email = email
#         self.phone = phone
#     def prLista():
#         for elev in Eleverlista:
#             print(f'Elevnamn: {elev.name}')

        
# ExternData = requests.get("https://dummyjson.com/users")

# InternData = ExternData.text

# PythonData = json.loads(InternData)

# Eleverlista = []
# EleverlistaUP = []

# for delar in PythonData["users"]:
#     HittaElever: elever = elever(
#         name=delar["firstName"], 
#         lastname=delar["lastName"], 
#         email=delar["email"],
#         phone=delar["phone"]
#     )
#     EleverlistaUP.append(HittaElever)



# for user in json_data["users"]:
#     EnElev = Person(
#         name=user["firstName"], 
#         lastname=user["lastName"], 
#         email=user["email"],
#         phone=user["phone"]
#         )
#     Elever.append(EnElev)




#Ny kommentar

