from pyperclip import copy
from random import choice
import string


def copy_pass(field_content):
    if field_content != "":
        copy(field_content)
    else:
        pass


def password_generation(length):
    password_gen = string.ascii_letters + string.digits
    password = "".join([choice(password_gen) for _ in range(length)])
    return password


def id_found(entries, id_no):
    for entry in entries:
        if id_no == entry[0]:
            print(id_no)
            print(entry[0])
            return True
