import dummy_data_generator

def run():
    columns = [
        {"name": "userId", "type": "ID"},
        {"name": "username", "type": "Name"},
        {"name": "email", "type": "Email"},
        {"name": "password", "type": "Password"},
        {"name": "createdon", "type": "Date", "start_date": "2020-01-01", "end_date": "2023-01-01"},
    ]
    num_rows = 25
    output_format = 'json'  # or 'xml'

    dummy_data_generator.generate_dummy_data(columns, num_rows, output_format)

if __name__ == '__main__':
    run()