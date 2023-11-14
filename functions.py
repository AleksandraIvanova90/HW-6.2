import re


def name_change(contacts_list):
    name_pattern = r'([А-Я])'
    name_substitution = r' \1'
    for column in contacts_list[1:]:
        line = column[0] + column[1] + column[2]
        k = re.sub(name_pattern, name_substitution, line).split()
        if len(k) == 3:
            column[0] = k[0]
            column[1] = k[1]
            column[2] = k[2]
        elif len(k) == 2:
            column[0] = k[0]
            column[1] = k[1]
            column[2] = ''
        elif len(k) == 1:
            column[0] = k[0]
            column[1] = ''
            column[2] = ''
    return contacts_list

def formatting_phone(contacts_list):
    phone_pattern = re.compile(
            r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_substitution = r'+7(\2)\3-\4-\5\7\8\9'
    for column in contacts_list[1:]:
        column[5] = phone_pattern.sub(phone_substitution, column[5])
    return

def duplicates_combining(contacts_list):
    l = {}
    for column in contacts_list[1:]:
        first_name = column[0]
        last_name = column[1]
        for contact in contacts_list:
            new_first_name = contact[0]
            new_last_name = contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if column[2] == '':
                    column[2] = contact[2]
                if column[3] == '':
                    column[3] = contact[3]
                if column[4] == '':
                    column[4] = contact[4]
                if column[5] == '':
                    column[5] = contact[5]
                if column[6] == '':
                    column[6] = contact[6]
        if column[0]+column[1] not in list(l.keys()):
            l[column[0]+column[1]] = column
    new_list = list(l.values())
    return l