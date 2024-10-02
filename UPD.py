#Importera bibliotek

import requests
import json

class Elev:
    def __init__ (self, name: str, lastname: str, email: str, phone: str, address: str):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.address = address
#För att struktera adressinformationen
    def adress_info(self):
        adress = self.address
        print(f"Adress: {adress['address']}, {adress['city']}, {adress['state']} {adress['postalCode']}, {adress['country']}")




#Get-förfrågan för att hämta data från API't.
extern_data = requests.get("https://dummyjson.com/users")

data = extern_data.text
#Omvandla API-svaret till Python-objekt
json_data = json.loads(data)


#Tom lista för elever
elever = []

# Loopa genom alla användare (user) i "users"-listan från JSON-data och
# skapa ett Elev-objekt av varje användare, som läggs till i listan elever.

for user in json_data["users"]:
    elev = Elev(
        name = user["firstName"],
        lastname = user["lastName"],
        email = user["email"],
        phone = user["phone"],
        address = user["address"]
    )
    elever.append(elev)

print(r"""
Välkommen till Grupp4:s sökverktyg och elevdatabas! 
Här kan du enkelt ta ut en klasslista eller söka en specifik elev för elevens kontaktuppgifter.

         _.-----._
       .'.-'''''-.'._
      //`         ` ;; 
     ;; '           ;;'.__.===============,
     ||  LOADING...  ||  __                 )
     ;;             ;;.'  '==============='
      \            ///
       ':.._____..:'~
         `'-----'`



Var god och logga in med de uppgifter du har fått från Grupp4.""")

def inloggning(användarnamn: str = "Devops24", lösenord: str = "Grupp4"):
    while True:
        angivet_namn = input("Användarnamn: ")
        angivet_lösenord = input("Lösenord: ")
        if angivet_namn == användarnamn and angivet_lösenord == lösenord:
            print("Du loggas in...")
            break
        else:
            print("Felaktig användarnamn eller lösenord! Försök igen")
inloggning()

#Sökningsfunktion
def söka_elev():
    elev_sökning = input("Ange elevens förnamn: ").lower()
    for sökning in elever:
        if sökning.name.lower() == elev_sökning:
            print("Sökningsresultat: ")
            print(f"Namn: {sökning.name} {sökning.lastname}")
            sökning.adress_info()
            print(f"Email: {sökning.email}, Telefon: {sökning.phone}\n")
            break
    else:
        print("Ingen elev med det angivna namnet kunde hittas.")
#         annan_elev = input("Vill du söka efter en annan elev? Svara \"ja\" eller \"nej\": ").lower()
#         if annan_elev != "ja":
#             print('''
# ****** Återgår till huvudmenyn. ******''')
#             break
def loopasök_elev():
    söka_elev()
    while True:
        Skajagloop=input('Vill du söka upp en annan elev? : ').lower()
        if Skajagloop == 'ja':
            söka_elev()
            continue
        elif Skajagloop == 'nej':
            break
        else:
            print('felaktigt svar, frågar igen')
            continue

def huvudmeny():
    while True:
        print(r'''
╦ ╦┬ ┬┬  ┬┬ ┬┌┬┐┌┬┐┌─┐┌┐┌┬ ┬
╠═╣│ │└┐┌┘│ │ │││││├┤ │││└┬┘
╩ ╩└─┘ └┘ └─┘─┴┘┴ ┴└─┘┘└┘ ┴

1. Klasslista
2. Sök elev
3. Logga ut
               ''')

        val: str = input("Ange menyvalet (1, 2 eller 3): ")
        if val == "1":
            print("\nKlasslista: ")
            for elev in elever:
                print(f"Namn: {elev.name} {elev.lastname}")
                elev.adress_info()
                print(f"Email: {elev.email}, Telefon: {elev.phone}\n")
            print('''
****** Slut på klasslistan. Återgår till huvudmenyn. ******\n''')

        elif val == "2":
           while True:
               loopasök_elev()
               break
        elif val == "3":
            print("Du loggas ut... ")
            break

        else:
            print("Ogiltigt val. Vänligen ange 1, 2 eller 3.")

    print("\nProgrammet avslutas. Ha en bra dag!")

huvudmeny()
