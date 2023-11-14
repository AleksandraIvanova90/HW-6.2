import csv

from functions import name_change, formatting_phone, duplicates_combining

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    name_change(contacts_list)
    formatting_phone(contacts_list)
    new_list = list(duplicates_combining(contacts_list).values())
    with open("phonebook.csv", 'w', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_list)


