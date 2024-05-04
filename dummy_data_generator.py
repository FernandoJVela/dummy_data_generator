import random
import json
import xml.etree.ElementTree as ET

def generate_random_data(columns, num_rows):
    data = []
    for _ in range(num_rows):
        row = {}
        for col in columns:
            if col['type'] == 'Currency':
                row[col['name']] = round(random.uniform(1, 1000), 2)
            elif col['type'] == 'Percentage':
                row[col['name']] = round(random.uniform(0, 100), 2)
            elif col['type'] == 'Integer':
                row[col['name']] = random.randint(1, 100)
            elif col['type'] == 'String':
                row[col['name']] = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=8))
            # Add more types as needed
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