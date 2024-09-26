#MAIN Branch
# import requests
# import json
import re


Name_Pattern =re.compile(r'\"firstName\"\:\s\"[A-Z,a-z]+\"')
name_P2 = re.compile(r'[A-Z,a-z]+')
# Found_Name_Pattern=Name_Pattern.finditer()



# Dummy_Import = requests.get('https://dummyjson.com/users')
# Dummy_Data: dict = Dummy_Import.json()

# print(Dummy_Data)

# # Chosen_Data: dict = json.loads(Dummy_Data)








#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
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



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#byggd med hjälp av shilans kod, har försökt att förtydliga vissa saker men varierande variabelnamn, byggt upp en inloggning, skapat en lista med namn mail och telefonnummer
import requests
import json

 
class elever:
    def __init__(self, name, lastname, email, phone ): #varför behövs allt annat en self?
        self.name = name
        self.lastname = lastname
        self.email = email
        self.phone = phone
    def prLista():
        for elev in Eleverlista:
            print(f'Elevnamn: {elev.name}')

        
ExternData = requests.get("https://dummyjson.com/users")

InternData = ExternData.text

PythonData = json.loads(InternData)

Eleverlista = []

for delar in PythonData["users"]:
    HittaElever = elever(
        name=delar["firstName"], 
        lastname=delar["lastName"], 
        email=delar["email"],
        phone=delar["phone"]
    )
    Eleverlista.append(HittaElever)



# for user in json_data["users"]:
#     EnElev = Person(
#         name=user["firstName"], 
#         lastname=user["lastName"], 
#         email=user["email"],
#         phone=user["phone"]
#         )
#     Elever.append(EnElev)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Inloggning för lärare
while True:
    lognamn=input('Namn: ').lower()
    logkod=input('Lösenord: ')
    if lognamn == 'john' and logkod=='Examen2026':
        print('Välkomen lärare John')
        break
    else:
        print('Inloggning misslyckad')

for elev in Eleverlista:
    print(f'elevnamn: {elev.name} {elev.lastname} , Mail: {elev.email} , Telefon: {elev.phone} ')



