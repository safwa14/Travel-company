print("""
╔═══╦╗─╔═══╗───╔═╗────────╔════╗──────────────╔═══╗
║╔═╗║║─║╔═╗║───║╔╝────────║╔╗╔╗║──────────────║╔═╗║
║║─║║║─║╚══╦══╦╝╚╦╗╔╗╔╦══╗╚╝║║╠╩═╦╗╔╦═╦╦══╦╗╔╗║║─╚╬══╦╗╔╦══╦══╦═╗╔╗─╔╗
║╚═╝║║─╚══╗║╔╗╠╗╔╣╚╝╚╝║╔╗║──║║║╔╗║║║║╔╬╣══╣╚╝║║║─╔╣╔╗║╚╝║╔╗║╔╗║╔╗╣║─║║
║╔═╗║╚╗║╚═╝║╔╗║║║╚╗╔╗╔╣╔╗║──║║║╚╝║╚╝║║║╠══║║║║║╚═╝║╚╝║║║║╚╝║╔╗║║║║╚═╝║
╚╝─╚╩═╝╚═══╩╝╚╝╚╝─╚╝╚╝╚╝╚╝──╚╝╚══╩══╩╝╚╩══╩╩╩╝╚═══╩══╩╩╩╣╔═╩╝╚╩╝╚╩═╗╔╝
────────────────────────────────────────────────────────║║───────╔═╝║
────────────────────────────────────────────────────────╚╝───────╚══╝
""")
print("Welcome to Al Safwa Tourism Company.")
days = int(input("How many days will you stay?"))
preference = input("Do you prefere a sea or mountain view?").lower()
budget = input("Is your budget large, medium or small?" ).lower()
if preference == "sea" :
    if budget == "large" :
        print("We recommend Maldives.🏝️ 🏝️ 🏝️")
    elif budget == "medium":
        print("We recommend Turkiye. 🏖️ 🏖️ 🏖️")    
    elif budget == "small" :
        print("We recommend Dahab. 🌅 🌅 🌅") 
    else :
        print("Sorry, This is not one of the options offered to you.🙅‍♀️")   
elif preference == "mountain":
    if budget == "large" :
        print("We suggest you visit Switzerland. 🏞️ 🏞️ 🏞️")
    elif budget == "medium" : 
        print("We suggest you visit Georgia. 🌄 🌄 🌄") 
    elif budget == "small" :
        print("We suggest you visit Mount St.Catherine. 🏔️ 🏔️ 🏔️ ")
    else :
        print("Sorry, This is not one of the options offered to you.🙅‍♀️") 
else:
    print("Sorry, This is not of our travel destinations. 🙅‍♂️")

print("Thank you for choosing our company.😊")           

              
               