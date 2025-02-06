import sys

'''
Missing functionalities:
1. Modifying existing item
2. Operate on units and quantities
'''

'''
class GroceryItem:
    def __init__(self, ItemName: str, Measure: float, Unit: str) -> None:
        self.ItemName = ItemName
        self.Measure = Measure
        self.Unit = Unit

    def describe(self) -> None:
        print(f'Selected item: "{self.ItemName}", which is in amount of {self.Measure} {self.Unit}.')

banana : GroceryItem = GroceryItem('Banana',2,'kg')
banana.describe()
sys.exit()
'''

global_option_list: list[str] = ['0','1','2','3','5']

def print_separator_bar(bar_string_length : int = 30) -> None:
    bar_string : str = bar_string_length * '-'
    return  print(bar_string)

def welcome_message() -> None:
    print('Welcome to Groceries list.')
    print_separator_bar()
    print('Enter:')
    print('1 - To add an item:')
    print('2 - To remove an item:')
    print('3 - To display the whole shopping list:')
    print('5 - To clear the shopping list:')
    print('0 - To exit the program:')
    print_separator_bar()

def exit_app() -> None:
    # Triggered by: 0
    print('Thank you for using the app. Goodbye!')
    sys.exit()

def add_item(item: str, groceries: list[str]) -> None:
    # Triggered by: 1
    if len(item) == 0:
        print("No item name was provided and no item was added to the shopping list.")
        #add_item()
    elif item in groceries:
        print(f'"{item}" is already in the shopping list.')
    else:
        groceries.append(item)
        print(f'"{item}" has been added to shopping list.')
    print_separator_bar()

def remove_item(item: str, groceries: list[str]) -> None:
    # Triggered by: 2
    try:
        groceries.remove(item)
        print(f'"{item}" has been removed from a shopping list.')
        print_separator_bar()
    except ValueError:
        print(f'There was not "{item}" on the shopping list.')
        print(f'There are fooling items on the shopping list: {groceries}')
        print_separator_bar()
    except Exception as e:
        print(f'{type(e)} - Error: {e}')
        print_separator_bar()

def modify_item(item: str, groceries: list[str]) -> None:
    # Triggered by: 5
    modified_item : int = int(input('Please select an item ID that you want to modify:'))
    if modified_item not in groceries:
    # missing try/except block - user input can be invalid
        print(f'Please provide valid number. Provided value: {item} is not a valid ID of item.')
    else:
        print(f'Item has been modified.')

    print_separator_bar()

def display_shopping_list(groceries: list[str]) -> None:
    # Triggered by: 3
    if len(groceries) == 0:
        print("There are no items to be deleted the shopping list.")
    else:
        print('---SHOPPING LIST---')
        for i, item in enumerate(groceries, 1):
            print(f'{i}: {item.capitalize()}')
    print_separator_bar(10)

def is_an_option(text: str) -> bool:
    return text in global_option_list

def clear_groceries_list(groceries: list[str]) -> None:
    # Triggered by: 5
    if len(groceries) == 0:
        print("There are no items to be deleted the shopping list.")
    else:
        # add functionality to make sure that user want's to do that
        groceries.clear()
        print(f'The shopping list has been cleared.')
    print_separator_bar()
#     groceries = []

def main() -> None:
    groceries: list[str] = []
    welcome_message()
    while True:
        user_input: str = input("Choose: ")

        if not is_an_option(user_input):
            print('Please pick a valid option.')
            continue

        match user_input:
            case '0':
                exit_app()
            case '1':
                new_item : str = input('What item would you like to add? >>').lower()
                add_item(new_item, groceries)
            case '2':
                cancelled_item : str = input('What item would you like to remove? >>').lower()
                remove_item(cancelled_item, groceries)
            case '3':
                display_shopping_list(groceries)
            case '5':
                clear_groceries_list(groceries)

if __name__ == '__main__':
    main()
