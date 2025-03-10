import json
import os
import datetime


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
    new_offer['date'] = input ('unesite datum u formatu YYYY-MM-DD (npr.2024-11-01): ')
    # proizvodi
    os.system('cls')
    print ('izaberite id ispred proizvoda da bi ga dodali u ponudu\n\n')
    proizvodi = []
    id = 1
    while True:
        print_product_list(products)
        entered_id = int(input ('unesite id proizvoda: '))
        
        for i in products:
            #print (type(i['id']))
            if i['id'] == entered_id:
                print (f"dodali ste: {i['name']} ")
                proizvod = {'product_id' : '','product_name' : '','description' : '','price' : 0,'quantity' : 0,'item_total' : 0}
                proizvod['product_id'] = id
                proizvod['product_name'] = i['name']
                proizvod['description'] = i['description']
                proizvod['price'] = i['price']
                proizvod['quantity'] = int(input ('upisite kolicinu: '))
                proizvod['item_total'] = i['price'] * proizvod['quantity']
                proizvodi.append(proizvod)
                id = id + 1
                #print (proizvod)
                #print (proizvodi)
            elif entered_id == 'x':
                break
        more_prod = input('zelite li dodati novi proizvod? da/ne ')
        if more_prod == 'da':
            continue
        else:
            break
    new_offer['items'] = proizvodi
    # Izračunajte sub_total, tax i total
    proizvod_cijena = 0.0

    for i in proizvodi:
        proizvod_cijena = proizvod_cijena + i['item_total']
    
    new_offer['sub_total'] = proizvod_cijena
    new_offer['tax'] = proizvod_cijena * 0.1
    new_offer['total'] = new_offer['sub_total'] + new_offer['tax']

    print (new_offer)
    
    # Dodajte novu ponudu u listu offers
    #data = load_data('offers.json')
    #data.append(new_offer)
    #save_data('offers.json', data)
    offers.append(new_offer)

# TODO: Implementirajte funkciju za upravljanje proizvodima.
def manage_products(products):
    """
    Allows the user to add a new product or modify an existing product.
    """
    new_product = {}
    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    os.system('cls')
    while True:
        print("1. Dodajte novi proizvod")
        print("2. Promjenite postojeci proizvod")
        print("3. Izlaz")
        print('\n\n')
        choice = input("Odabrana opcija: ")
    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
        if choice == "1":
            new_product['id'] = len(products)+1
            new_product['name'] = input('unesite ime proizvoda: ')
            new_product['description'] = input('unesite opis proizvoda: ')
            new_product['price'] = float(input('unesite cijenu proizvoda: '))
            products.append(new_product)

            #data = load_data('products.json')
            #data.append(new_product)
            #save_data('products.json', data)

    # Za izmjenu: selektirajte proizvod i ažurirajte podatke
        elif choice == "2":
            for i in products:
                print (f"{i['id']} - {i['name']}")
         
            id = int(input ('\nodaberite id pored proizvoda koji zelite promjeniti:\n'))
            for i in products:
                #print (type(i['id']))
                #print (type(id))
                if i['id'] == id:
                    i['name'] = input('upisite novo ime: ')
                    i['description'] = input('upisite novi opis: ')
                    i['price'] = float(input('upisite novu cijenu: '))
            for i in products:
                print (f"{i['id']} - {i['name']}")            
        elif choice == "3":
            break


# TODO: Implementirajte funkciju za upravljanje kupcima.
def manage_customers(customers):
    """
    Allows the user to add a new customer or view all customers.
    """
    new_customer = {}
    os.system('cls')
    while True:
        print("1. Dodajte novog kupca")
        print("2. Izlistajte kupce")
        print("3. Izlaz")
        print('\n\n')
        choice = input("Odabrana opcija: ")
    # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
        if choice == "1":
            new_customer['name'] = input('unesite ime kupca: ')
            new_customer['email'] = input('unesite email kupca: ')
            new_customer['vat_id'] = input('unesite vat_id: ')
            customers.append(new_customer)
            

            #data = load_data('customers.json')
            #data.append(new_customer)
            #save_data('customers.json', data)
    # Za pregled: prikaži listu svih kupaca
        elif choice == "2":
            for i in customers:
                print (f"{i['name']} - {i['email']} - {i['vat_id']}")
        elif choice == "3":
            break


# TODO: Implementirajte funkciju za prikaz ponuda.
def display_offers(offers):
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    os.system('cls')
    while True:
        print("1. prikazi sve ponude")
        print("2. pregledaj ponude po mjesecima")
        print("3. pregledaj ponudu po IDu")
        print("4. Izlaz")
        print('\n\n')
        choice = input("Odabrana opcija: ")
        if choice == "1":
            for i in offers:
                #print (i)
                print(f"Ponuda br: {i['offer_number']}, Kupac: {i['customer']}, Datum ponude: {i['date']}")
                print("Stavke:")
                for item in i["items"]:
                    print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
                    print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
                print(f"Ukupno: ${i['sub_total']}, Porez: ${i['tax']}, Ukupno za platiti: ${i['total']}\n")
        elif choice == "2":
            month = int(input('upisi broj mjeseca za koji zelis pregledati ponude: '))
            offer_by_month = []
            for i in offers:
                if datetime.datetime.strptime(i['date'], '%Y-%m-%d').month == month:
                    offer_by_month.append(i)

            for i in offer_by_month:
                #print (i)
                print(f"Ponuda br: {i['offer_number']}, Kupac: {i['customer']}, Datum ponude: {i['date']}")
                print("Stavke:")
                for item in i["items"]:
                    print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
                    print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
                print(f"Ukupno: ${i['sub_total']}, Porez: ${i['tax']}, Ukupno za platiti: ${i['total']}\n")
  

            '''# Desired month (e.g., March)
            desired_month = 3

            # Filter list members based on the desired month
            filtered_data = [item for item in data if datetime.datetime.strptime(item['date'], '%Y-%m-%d').month == desired_month]

            print(filtered_data)
            '''
        elif choice == "3":
            id = int(input('upisi id ponude koju zelis pregledati: '))
            for i in offers:
                if id == i['offer_number']:
                    print(f"Ponuda br: {i['offer_number']}, Kupac: {i['customer']}, Datum ponude: {i['date']}")
                    print("Stavke:")
                    for item in i["items"]:
                        print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
                        print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
                    print(f"Ukupno: ${i['sub_total']}, Porez: ${i['tax']}, Ukupno za platiti: ${i['total']}\n")
        elif choice == "4":
            break


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

#def print_all_offers(offer):

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
