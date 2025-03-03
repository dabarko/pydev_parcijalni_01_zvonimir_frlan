import json
import os


OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"


def load_data(filename):
    """Load data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {filename}. Check file format.")
        return []


def save_data(filename, data):
    """Save data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# TODO: Implementirajte funkciju za kreiranje nove ponude.
def create_new_offer(offers, products, customers):
    """
    Prompt user to create a new offer by selecting a customer, entering date,
    choosing products, and calculating totals.
    """
    new_offer = {}

    # iduci offers id
    new_offer['offer_number'] = len(offers)+1

    # Omogućite unos kupca
    os.system('cls')
    print ('Unesite kupca iz liste:\n')
    kupci = []
    for i in customers:
        print(i['name'])
        kupci.append(i['name'])
    print('\n')
    new_offer['customer'] = input('kupac: ')
    while True: 
        if new_offer['customer'] not in kupci:
            os.system('cls')
            for i in customers:
                print(i['name'])
            new_offer['customer'] = input('\nunesite postojeceg kupca: ')
        else:
            break
    # datum
    os.system('cls')
    new_offer['date'] = input ('unesite datum u formatu YYYY-MM-DD (npr.2024-11-01)')
    # proizvodi
    os.system('cls')
    print ('izaberite id ispred proizvoda da bi ga dodali u ponudu\n\n')
    proizvodi = []
    proizvod = {'product_id' : '','product_name' : '','description' : '','price' : 0,'quantity' : 0,'item_total' : 0}
    proizvod_cijena = 0.0
    porez = 1.1
    proizvodi_total = proizvod_cijena * porez

    while True:
        print_product_list(products)
        entered_id = int(input ('unesite id proizvoda: '))
        kolicina = int(input ('upisite kolicinu: '))
        id = 1
        for i in products:
            #print (type(i['id']))
            if i['id'] == entered_id:
                print (f"dodali ste: {i['name']} ")
                proizvod['product_id'] = id
                proizvod['product_name'] = i['name']
                proizvod['description'] = i['description']
                proizvod['price'] = i['price']
                proizvod['quantity'] = kolicina
                proizvod['item_total'] = i['price'] * proizvod['quantity']
                proizvodi.append(proizvod)
                print (proizvod)
                print (proizvodi)
            elif entered_id == 'x':
                break
        more_prod = input('zelite li dodati novi proizvod? da/ne')
        if more_prod == 'da':
            continue
        else:
            break

'''    print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
         "id": 2,
        "name": "Smartphone",
        "description": "6-inch display, 128GB storage",
        "price": 500.0'''
    # Izračunajte sub_total, tax i total

    # Dodajte novu ponudu u listu offers
    


# TODO: Implementirajte funkciju za upravljanje proizvodima.
def manage_products(products):
    """
    Allows the user to add a new product or modify an existing product.
    """
    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
    # Za izmjenu: selektirajte proizvod i ažurirajte podatke
    pass


# TODO: Implementirajte funkciju za upravljanje kupcima.
def manage_customers(customers):
    """
    Allows the user to add a new customer or view all customers.
    """
    # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
    # Za pregled: prikaži listu svih kupaca
    pass


# TODO: Implementirajte funkciju za prikaz ponuda.
def display_offers(offers):
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    # Prikaz relevantnih ponuda na temelju izbora
    pass


# Pomoćna funkcija za prikaz jedne ponude
def print_offer(offer):
    """Display details of a single offer."""
    print(f"Ponuda br: {offer['offer_number']}, Kupac: {offer['customer']['name']}, Datum ponude: {offer['date']}")
    print("Stavke:")
    for item in offer["items"]:
        print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
        print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
    print(f"Ukupno: ${offer['sub_total']}, Porez: ${offer['tax']}, Ukupno za platiti: ${offer['total']}")

def print_product_list(products):
    for i in products:
        print(f"{i['id']} - {i['name']} - {i['description']} - {i['price']}")
    print('za prekid unesite x\n\n')


def main():
    # Učitavanje podataka iz JSON datoteka
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)

    while True:
        print("\nOffers Calculator izbornik:")
        print("1. Kreiraj novu ponudu")
        print("2. Upravljanje proizvodima")
        print("3. Upravljanje korisnicima")
        print("4. Prikaz ponuda")
        print("5. Izlaz")
        choice = input("Odabrana opcija: ")

        if choice == "1":
            create_new_offer(offers, products, customers)
        elif choice == "2":
            manage_products(products)
        elif choice == "3":
            manage_customers(customers)
        elif choice == "4":
            display_offers(offers)
        elif choice == "5":
            # Pohrana podataka prilikom izlaza
            save_data(OFFERS_FILE, offers)
            save_data(PRODUCTS_FILE, products)
            save_data(CUSTOMERS_FILE, customers)
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")


if __name__ == "__main__":
    main()
