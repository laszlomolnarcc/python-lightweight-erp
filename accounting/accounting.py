# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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
    options = ["Show accounting table",
               "Adding new record",
               "Removing record",
               "Updating record",
               "Show year of highest profit",
               "Show average profit for a year"]
    ui.print_menu("Accounting menu", options, "Back to main menu")


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
        ui.print_result(str(which_year_max(table)),
                        "The year with most profit is: ")
    elif option == "6":
        year = ui.get_inputs(["Please enter the year: "])[0]
        ui.print_result(str(avg_amount(table, int(year))),
                        "Average profit per item in given year: ")
    elif option == "0":
        return "stop"
    else:
        raise KeyError("There is no such option.")

# print the default table of records from the file
#
# @table: list of lists


def show_table(table):
    title_list = ["Id", "Month", "Day", "Year", "Type", "Amount"]
    ui.print_table(table, title_list)
    return table


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    new_record = ui.get_inputs(
        ["Month: ", "Day: ", "Year: ", "Type: ", "Amount (dollar): "], "")
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
        ["Month: ", "Day: ", "Year: ", "Type: ", "Amount (dollar): "], "")
    return common.update_row(table, id_, update_data)


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
