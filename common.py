# implement commonly used functions here

import random


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)
def generate_random(table):
    special_chars = ["%", "!", "#", "$", "&"]
    generated = ""
    while(generated == "" or generated in [x[0] for x in table]):
        generated = ""
        abc = [[str(i) for i in range(0, 10)],
               [chr(i) for i in range(65, 91)],
               [chr(i) for i in range(97, 123)],
               special_chars]
        for i in range(-5, 8, 2):
            generated += random.choice(abc[abs(i) // 2])
        generated += random.choice(abc[3])
    return generated


def add_row(table, new_row):
    item_id = generate_random(table)
    return table + [[item_id] + new_row]


def remove_row(table, _id):
    result_table = table[:]
    for idx, row in enumerate(result_table):
        if row[0] == _id:
            del result_table[idx]
            break
    return result_table


def update_row(table, _id, update_list):
    result_table = table[:]
    for idx, row in enumerate(result_table):
        if row[0] == _id:
            result_table[idx] = [_id] + update_list
    return result_table


def sum_of_elements(sum_list):
    result = 0
    for item in sum_list:
        result += item
    return result
