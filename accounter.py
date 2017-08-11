import re
import csv
menu = '''
    Choose your destiny:
    [1] - Add record
    [2] - Show report
    [3] - Export to csv
    [4] - Exit
    '''
submenu = '''
    How do you want to do it?
    [1] - All records
    [2] - Records for specific date
    [3] - Records for category
    [4] - Records with amount more or less than value
    '''
menu_options = '1234'
submenu_options = '1234'


def main():
    initialize_file('accounterdata.csv')
    while True:
        print(menu)
        selected = read_option(menu_options)
        if(selected == '1'):
            add_record()
        elif(selected == '2'):
            create_report('screen')
        elif(selected == '3'):
            create_report('file')
        elif(selected == '4'):
            break


def initialize_file(file_name):
    with open(file_name, 'a'):
        return


def read_option(available_options):
    option = input('What do you want to do? ')
    while (len(option) > 1 or option not in available_options):
        print('Something wrong!')
        option = input('What do you want to do? ')
    return option


def add_record():
    date = read_date("Enter date in a valid format (DD-MM-YYYY): ")
    category = read_category("Enter category of expences: ")
    amount = read_amount("Enter amount spent: ")
    with open('accounterdata.csv', 'a', newline='') as file:
        writter = csv.writer(file)
        writter.writerow([date, category, amount])


def read_date(note='>>'):
    date = ''
    while(re.match('[0-3][0-9]-[0-1][0-9]-[0-9][0-9][0-9][0-9]', date)is None):
        date = input(note)
    return date


def read_category(note='>>'):
    category = ''
    while(len(category) <= 0):
        category = input(note)
    return category


def read_amount(note='>>'):
    amount = ''
    while(len(amount) <= 0 or re.match("^-?\\d*(\\.\\d+)?$", amount) is None):
        amount = input(note)
    return float(amount)


def read_amount_value(value, note='>>'):
    amount = ''
    while(len(amount) <= 0 or re.match("^-?\\d*(\\.\\d+)?$", amount) is None):
        amount = input(note)
        if(amount == ''):
            return value
    return float(amount)


def create_report(output):
    print(submenu)
    selected = read_option(submenu_options)
    if(selected == '1'):
        data = read_all_data()
    elif(selected == '2'):
        data = read_date_data()
    elif(selected == '3'):
        data = read_category_data()
    elif(selected == '4'):
        data = read_amount_data()
    if(output == 'screen'):
        print('Date\t\t\tCategory\t\t\tAmount')
        for row in data:
            print('\t\t'.join(row))
    elif(output == 'file'):
        export_csv(data)


def read_all_data(file_name='accounterdata.csv'):
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


def read_date_data(file_name='accounterdata.csv'):
    date = read_date("For which date? ")
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[0] == date):
                data.append(row)
    return data


def read_category_data(file_name='accounterdata.csv'):
    cat = read_category("Which category to search for? ")
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[1] == cat):
                data.append(row)
    return data


def read_amount_data(file_name='accounterdata.csv'):
    min_a = read_amount_value(0, """
    Provide minimal amount (or press 'Enter' to set 0 by default):
    """)
    max_a = read_amount_value(100e100, """
    Provide max amount (or press 'Enter' to set no max limit by default):
    """)
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if(min_a <= float(row[2]) <= max_a):
                data.append(row)
    return data


def read_filename():
    file_name = ''
    while(len(file_name) <= 0 or re.match("^[\w\-. ]+$", file_name) is None):
        file_name = input("Provide file name to save records: ")
    return file_name + '.csv'


def export_csv(records):
    file_name = read_filename()
    with open(file_name, 'w', newline='') as file:
        wr = csv.writer(file)
        for item in records:
            wr.writerow(item)


if __name__ == '__main__':
    main()
