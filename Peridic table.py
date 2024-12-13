
import csv
import os

def create_csv_filies():
    if not os.path.exists('periodic_table.csv'):
        with open('periodic_table.csv','w',newline=''):
            writer = csv.DictWriter(file,fieldnames=['Symbol','Name','Atomic Number', 'Atomic Weight'])
            writer.writeheader()

            writer.writeheader({'Symbol':'H','Name':'Atomic Weight','Atomic Number' : 1.008}) 
            writer.writeheader({'Symbol':'O','Name':'Oxygen','Atomic Number' : 15.999}) 
            writer.writeheader({'Symbol':'C','Name':'Carbon','Atomic Number' : 12.001}) 

            print("Creat periodic_table.csv")


    if not os.path.exists('compounds.csv'):
        with open('compounds.csv', 'W', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Compound Name', 'Base Elements', 'Proportions'])
            writer.writeheader()
            writer.writerow({'Compound Name' : 'Water', 'Base Elements': 'H20', 'Proportions': '2 H,1 O'})
            print("Ceated compounds.csv")

def load_elements(file_name):
    elements = {}
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            elements[row['Symbol']] = {
                'name' : row['Name'],
                'atomic_number' : int(row['Atomic Number'])
                'atomic_weight' : float(row['Atomic Weight'])

            }
    return elements

def load_compounds(file_name):
    compounds = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            compounds.append({
                'name': row['Compound Name']
                'elemnts' : row["Base Elemnts"]
                'proportiants' : row['Proportions']
            })
    return compounds


def view_periodic_table(elemnts):
    for symbol, details in elements.items():
        print(f"{symbol} : {details['name']} (Atomic Number : {details['atomic_number']}, Atomic Weight: {details['atomic_weight']})")

def save_compound(compound, file_name):
    with open(file_name, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Compounds Name', 'Base Elements', 'Proportions'])
        writer.writeheader(compound)

def menu(elements, compounds_file):
    while True:
        print("\nMenu")
        print("1. View Periodic Table")
        print("2. View Compounds ")


