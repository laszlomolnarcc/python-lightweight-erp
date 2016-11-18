# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


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
    options = ["Show table",
               "Add record to table",
               "Remove record from table",
               "Update a record in table",
               "Number of game types by manufacturer",
               "Number of games in stock by a given manufacturer"]

    ui.print_menu("Store Manager menu", options, "Main menu")


def choose():
    file_name = "store/games.csv"
    table = data_manager.get_table_from_file(file_name)
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        table = add(table)
        data_manager.write_table_to_file(file_name, table)
    elif option == "3":
        show_table(table)
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
        ui.print_result(get_counts_by_manufacturers(table),
                        "Number of game types in stock by manufacturer:")
    elif option == "6":
        manuf = ui.get_inputs(["Enter a manufacturer: "], "")
        average = str(get_average_by_manufacturer(table, manuf[0]))
        ui.print_result(
            average, "Average number of games in stock by {0}:".format(manuf[0]))
    elif option == "0":
        return "stop"
    else:
        raise KeyError("There is no such option.")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["ID", "Title", "Manufacturer", "Price", "Copies in stock"]
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    new_record = ui.get_inputs(
        ["Title: ", "Manufacturer: ", "Price: ", "Copies in stock: "], "")
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
    update_data = ui.get_inputs(
        ["Title: ", "Manufacturer: ", "Price: ", "Copies in stock: "], "")
    return common.update_row(table, id_, update_data)


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    # key: manufacturer, value: set of game types
    manufacturers_dict = {}
    for item in table:
        if item[2] in manufacturers_dict:
            manufacturers_dict[item[2]] += 1
        else:
            manufacturers_dict[item[2]] = 1
    return manufacturers_dict


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):
    amount_in_stock = 0
    titles_in_stock = 0

    for i in table:
        if i[2] == manufacturer:
            amount_in_stock += int(i[4])
            titles_in_stock += 1
    # the float() casting is not needed in python 3
    return amount_in_stock / float(titles_in_stock)
