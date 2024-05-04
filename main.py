import dummy_data_generator

def run():
    columns = [
        {"name": "ID", "type": "Integer"},
        {"name": "Name", "type": "String"},
        {"name": "Price", "type": "Currency"},
        {"name": "Discount", "type": "Percentage"}
    ]
    num_rows = 10
    output_format = 'json'  # or 'xml'

    dummy_data_generator.generate_dummy_data(columns, num_rows, output_format)

if __name__ == '__main__':
    run()