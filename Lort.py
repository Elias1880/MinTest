#Author: GRP. 25 - Case om kaffemaskine på KEA.

while True: #Får programmet til at køre i et loop.

    import time #Til at bruge længere nede ved betaling for at give illusionen af betaling registreres.

    class Kaffe:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def get_coffee(self):
            print(" You chose " + str(self.name) + " That will be " + str(self.price) + "DKK")
#En klasse, som hedder Kaffe og laver funktionen get_coffe.

    class Coin_sensor:
        def __init__(self):
            self.inserted_coins = []

        def add_coins(self, coins):
            self.inserted_coins.append(int(coins))
#En klasse, som hedder Coin_sensor for at vise hvordan en sensor ville opfange og tælle mønsterne.

    def Payment(): #Betalingens funktion
        print("\t1 - CASH \tOR\t2 - CARD?")
        x = input()

        a = Coin_sensor()

        def Coin_count(): #Ved betaling med danske mønter.
            b = 0
            while (b <= 9): #Prisen er 10, men sætter man 10 ind her, så vil den over 10. Ved at bruge 9, så stopper den ved 10.
                print("Insert coins")
                coins = input()
                a.add_coins(coins)
                print(a.inserted_coins)
                b = sum(a.inserted_coins)
                print(b)

            print("One moment please...\n")
            time.sleep(1)
            print("...")
            time.sleep(2)
            print("PAYMENT SUCCESSFUL")
            print("POURING...")
            time.sleep(2)
            print("""ENJOY YOUR COFFEE.
            THANK YOU, COME AGAIN!""")
            print("THANK YOU, COME AGAIN!")
            print("\n\n")

        if x == "1":
            Coin_count() #Kalder på funktionen

        if x == "2": #Ved kort betaling
            print("Confirm - y or n")
            x = input()
            if x == "y":
                print("AUTHORIZING...\n")
                time.sleep(1)
                print("...")
                time.sleep(2)
                print("PAYMENT SUCCESSFUL")
                print("POURING...")
                time.sleep(2)
                print("""ENJOY YOUR COFFEE.
                THANK YOU, COME AGAIN!""")
                print("\n\n")
            elif x == "n":
                print("---CANCELLED---")

    Espresso = Kaffe("Espresso", 10)
    Double_espresso = Kaffe("Double_espresso", 10)
    Cappuccino = Kaffe("Cappuccino", 10)
    Latte = Kaffe("Latte", 10)
    Americano = Kaffe("Americano", 10)
    Cortado = Kaffe("Cortado", 10)
    Cocoa = Kaffe("Cocoa", 10)
    Hot_water = Kaffe("Hot_water", 10)
#Vores valgliste af kaffe, som alle kalder på klassen, Kaffe. De har alle et navn og en pris.
    print("""WELCOME DEAR PERSON at KEA, WHAT DRINK WOULD YOU LIKE? PRICE: 10 DKK.
    1 ESPRESSO
    2 DOUBLE ESPRESSO
    3 CAPPUCCINO
    4 LATTE
    5 AMERICANO
    6 CORTADO
    7 COCOA
    8 HOT WATER
    \n""")
    choice = input()
#Beder bruger om valg af kaffe. Vi ser udvalget og input tages videre ned.
#Nederst ses hvordan den bruger navn til at kalde på en funktion i en klasse, plus kalde på betalingsfunktionen.

    if choice == "1":
        Espresso.get_coffee()
        Payment()
    elif choice == "2":
        Double_espresso.get_coffee()
        Payment()
    elif choice == "3":
        Cappuccino.get_coffee()
        Payment()
    elif choice == "4":
        Latte.get_coffee()
        Payment()
    elif choice == "5":
        Americano.get_coffee()
        Payment()
    elif choice == "6":
        Cortado.get_coffee()
        Payment()
    elif choice == "7":
        Cocoa.get_coffee()
        Payment()
    elif choice == "8":
        Hot_water.get_coffee()
        Payment()
