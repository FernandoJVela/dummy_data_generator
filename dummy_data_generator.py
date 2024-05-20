import random
import json
import xml.etree.ElementTree as ET
import os
import dummy_name_generator
from datetime import datetime, timedelta

def check_names_availability():
    names_file_path = "random_names.txt"
    if ~os.path.exists(names_file_path):
        random_names = dummy_name_generator.generate_full_names(100)
        dummy_name_generator.save_to_txt(random_names)

def get_random_name():
    with open("random_names.txt", 'r') as file:
        lines = file.readlines()
        return random.choice(lines).rstrip()
    
def generate_random_email():
    domains = ["example.com", "mail.com", "test.com"]
    name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=random.randint(5, 10)))
    domain = random.choice(domains)
    return f"{name.lower()}@{domain}"

def generate_random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")

def generate_random_password(length=12):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    password = ''.join(random.choices(characters, k=length))
    return password

def generate_random_data(columns, num_rows):
    check_names_availability()    
    data = []
    used_ids = set() 
    for _ in range(num_rows):
        row = {}
        for col in columns:
            if col['type'] == 'Currency':
                row[col['name']] = round(random.uniform(1, 1000), 2)
            elif col['type'] == 'Percentage':
                row[col['name']] = round(random.uniform(0, 1), 5)
            elif col['type'] == 'Integer':
                row[col['name']] = random.randint(1, 100)
            elif col['type'] == 'String':
                first_entry = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=random.randint(1, 10)))
                second_entry = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=random.randint(1, 10)))
                row[col['name']] = ''.join(first_entry + ' ' + second_entry)
            elif col['type'] == 'Name':
                row[col['name']] = get_random_name()
            elif col['type'] == 'ID':
                new_id = None
                while new_id is None or new_id in used_ids:
                    new_id = random.randint(1, num_rows*10)
                row[col['name']] = new_id
                used_ids.add(new_id)
            elif col['type'] == 'Email':
                row[col['name']] = generate_random_email()
            elif col['type'] == 'Date':
                start_date = datetime.strptime(col.get('start_date', '2000-01-01'), "%Y-%m-%d")
                end_date = datetime.strptime(col.get('end_date', '2020-12-31'), "%Y-%m-%d")
                row[col['name']] = generate_random_date(start_date, end_date)
            elif col['type'] == 'Password':
                row[col['name']] = generate_random_password()
        data.append(row)
    return data

def generate_dummy_data(columns, num_rows, output_format):
    data = generate_random_data(columns, num_rows)
    if output_format.lower() == 'json':
        with open('dummy_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
    elif output_format.lower() == 'xml':
        root = ET.Element("table")
        for row in data:
            row_element = ET.SubElement(root, "row")
            for key, value in row.items():
                col_element = ET.SubElement(row_element, key)
                col_element.text = str(value)
        tree = ET.ElementTree(root)
        tree.write('dummy_data.xml')