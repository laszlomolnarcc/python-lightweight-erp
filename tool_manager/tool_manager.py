# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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
# we need to reach the default and the special functions of this module
# from the module menu
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
    options = ["Tool database",
               "Add new tool",
               "Remove tool",
               "Update tool data",
               "Tool(s) within durability",
               "Durability time per manufacturer"]
    ui.print_menu("Tool manager", options, "Back to main menu")


def choose():
    file_name = "tool_manager/tools.csv"
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
        ui.print_result(get_available_tools(table), "Tools available:")
    elif option == "6":
        ui.print_result(get_average_durability_by_manufacturers(
            table), "Average durability per manufacturer:")
    elif option == "0":
        return "stop"
    else:
        raise KeyError("There is no such option.")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["ID", "Name", "Manufacturer", "Purchase date", "Durability"]
    ui.print_table(table, title_list)
    return table


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    new_record = ui.get_inputs(
        ["Name: ", "Manufacturer: ", "Purchase date: ", "Durability: "], "")
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
        ["Name: ", "Manufacturer: ", "Purchase date: ", "Durability: "], "")
    return common.update_row(table, id_, update_data)


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_tools(table):
    available_tools = []
    actual_year = int(ui.get_inputs(
        ["Current year: "], "")[0])
    for line in table:
        if int(line[3]) + int(line[4]) >= actual_year:
            available_tools.append(line)
    return available_tools


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):
    avg = {}
    for line in table:
        if line[2] in avg:
            avg[line[2]].append(int(line[4]))
        else:
            avg[line[2]] = [int(line[4])]
    for key, value in avg.items():
        avg[key] = common.sum_of_elements(value) / len(value)
    return avg
