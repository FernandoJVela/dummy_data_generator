import dummy_data_generator

def run():
    columns = [
        {"name": "ID", "type": "ID"},
        {"name": "Name", "type": "Name"},
        {"name": "Price", "type": "Currency"},
        {"name": "Discount", "type": "Percentage"},
        {"name": "Description", "type": "String"},
    ]
    num_rows = 10
    output_format = 'json'  # or 'xml'

    dummy_data_generator.generate_dummy_data(columns, num_rows, output_format)

if __name__ == '__main__':
    run()