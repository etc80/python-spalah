import re
import csv

def init_main_menu():
    main_menu = [
        ['Add record', add_record ],
        ['Show report', print_report_data ],
        ['Export to CSV', export_report_csv ],
        ['Exit', exit ]
    ]
    return main_menu

def init_submenu():
    submenu_report = [
        ['All records', read_all_data],
        ['Records for specific date', read_date_data ],
        ['Records for category', read_category_data ],
        ['Records with amount more or less than value', read_amount_data ]
    ]
    return submenu_report


def main():
    main_menu = init_main_menu()
    initialize_file('accounterdata.csv')
    while True:
        interact_with_menu(main_menu)


def interact_with_menu(menu):
    print_menu(menu)
    selected = read_option(menu)
    menu[selected][1]()


def print_menu(menu):
    i = 1
    for menuitem in menu:
        print(i, '-', menuitem[0])
        i += 1


def initialize_file(file_name):
    with open(file_name, 'a'):
        return


def read_option(menu):
    option = input('What do you want to do? ')
    available_options = ''.join( str(x) for x in list(range(1, len(menu)+1)))
    while (len(option) > 1 or option not in available_options):
        print('Something wrong!')
        option = input('What do you want to do? ')
    return int(option)-1


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


def create_report():
    submenu_report = init_submenu()
    print_menu(submenu_report)
    selected = read_option(submenu_report)
    data = submenu_report[selected][1]()
    return data


def print_report_data():
    data = create_report()
    print('Date\t\t\tCategory\t\t\tAmount')
    for row in data:
        print('\t\t'.join(row))


def export_report_csv():
    records = create_report()
    file_name = read_filename()
    with open(file_name, 'w', newline='') as file:
        wr = csv.writer(file)
        for item in records:
            wr.writerow(item)


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


if __name__ == '__main__':
    main()
