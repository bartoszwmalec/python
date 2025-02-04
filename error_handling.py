import sys, time

while True:
    try:
        user_input: str = input("Enter a number: ")
        print(f'10 / {user_input} = {10 / float(user_input)}')
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    except ValueError:
        print("Please enter a valid number...")
    except Exception as e:
        print(f"Error: {e}")
    # "else" is not recommended as it's executed after try/except block
    else:
        print("There were no exception encountered.")
    # "finally" code block is executed, even in case of failure of code above
    finally:
        print("Quit the program (disregards of what happened before).")
        time.sleep(1)
        sys.exit()
