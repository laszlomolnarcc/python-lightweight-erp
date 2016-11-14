

# This function needs to print outputs like this:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table
def print_table(table, title_list):
    # insert the title list to the start of the table
    table.insert(0, title_list)
    max_width_per_column = get_max_line_widths(table)
    # print table start row
    print(get_separator_line(max_width_per_column, "/", "-", "\\"))
    row_separator_line = get_separator_line(
        max_width_per_column, "|", "|", "|")
    # print table
    for idx in range(0, len(table)):
        print(get_row_string(table[idx], max_width_per_column))
        if idx < len(table) - 1:
            print(row_separator_line)
    # print table end row
    print(get_separator_line(max_width_per_column, "\\", "-", "/"))
    table.pop(0)  # remove the title list from table


def get_max_line_widths(table):
    max_width_per_column = [0] * len(table[0])
    for row in table:
        for idx in range(0, len(row)):
            if len(row[idx]) > max_width_per_column[idx]:
                max_width_per_column[idx] = len(row[idx])
    return max_width_per_column


def get_separator_line(max_width_per_column, start_char, in_line_sep, end_char):
    line = start_char
    for idx, width in enumerate(max_width_per_column):
        line += "-" * width
        if idx < len(max_width_per_column) - 1:
            line += in_line_sep
        else:
            line += end_char
    return line


def get_row_string(item_list, max_width_per_column):
    row_line = ""
    for idx, item in enumerate(item_list):
        row_line += "|{0:^{1}}".format(item, max_width_per_column[idx])
    return row_line + "|"


# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):
    print("\n{0}".format(label))
    if type(result) is str:
        print(result)
    elif type(result) is list:
        for i in result:
            print(i, sep=", ")
    elif type(result) is dict:
        for key in result:
            print("{0}: {1}".format(key, result[key]))
    print()

# This function needs to generate outputs like this:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")


def print_menu(title, list_options, exit_message):
    print(title + ":")
    for i, v in enumerate(list_options, 1):
        print("({0}) {1}".format(i, v))
    print("(0) {0}".format(exit_message))


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):
    if title != "":
        print(title)

    inputs = []
    for item in list_labels:
        inputs.append(input(item))
    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    print("Error: {0}".format(message))
