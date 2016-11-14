# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader(
    "data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader(
    "common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():
    #TODO: read table from file
    while True:
        handle_menu()
        try:
            choice = choose()
        except KeyError as err:
            ui.print_error_message(err)
        else:
            if choice == "stop":
                break


def handle_menu():
    options = ["Employee database",
               "Add new employee",
               "Remove employee",
               "Update employee data",
               "Oldest employee",
               "Employee with average age"]
    ui.print_menu("Human resources manager", options, "Back to main menu")


def choose():
    file_name = "hr/persons.csv"
    table = data_manager.get_table_from_file(file_name)
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]

    if option == "1":
        show_table(table)
    elif option == "2":
        table = add(table)
        data_manager.write_table_to_file(file_name, table)
    elif option == "3":
        remove_id = ui.get_inputs(
            ["Enter the ID of the record to be removed: "], "")
        table = remove(table, remove_id[0])
        data_manager.write_table_to_file(file_name, table)
    elif option == "4":
        show_table(table)
        update_id = ui.get_inputs(
            ["Enter the ID of the record to be updated: "], "")
        table = update(table, update_id[0])
        data_manager.write_table_to_file(file_name, table)
    elif option == "5":
        ui.print_result(get_oldest_person(table), "Oldest employee(s):")
    elif option == "6":
        ui.print_result(get_persons_closest_to_average(
            table), "Employee closest to average age:")
    elif option == "0":
        return "stop"
    else:
        raise KeyError("There is no such option.")

# print the default table of records from the file
#
# @table: list of lists


def show_table(table):
    title_list = ["ID", "Name", "Date of birth"]
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    new_record = ui.get_inputs(["Enter name: ", "Enter date of birth: "], "")
    return common.add_row(table, new_record)


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    return common.remove_row(table, id_)


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    update_data = ui.get_inputs(["Enter name:", "Enter date of birth:"], "")
    return common.update_row(table, id_, update_data)


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with
# the same value)
def get_oldest_person(table):
    min_birth_year = 999999  # set a big number as year
    for row in table:
        if int(min_birth_year) > int(row[2]):
            min_birth_year = row[2]

    oldest_employees = []
    for row in table:
        if min_birth_year in row:
            oldest_employees.append(row[1])
    return oldest_employees


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with
# the same value)
def get_persons_closest_to_average(table):
    # get the average age of employees
    avg = 0
    for item in table:
        avg += int(item[2])
    avg = avg / len(table)
    # get the smallest difference between birth years
    smallest_diff = avg * avg
    for row in table:
        current_diff = abs(int(row[2]) - avg)
        if current_diff < smallest_diff:
            smallest_diff = current_diff
    # create the final birth year list
    result = []
    for row in table:
        if abs(int(row[2]) - avg) == smallest_diff:
            result.append(row[1])
    return result
