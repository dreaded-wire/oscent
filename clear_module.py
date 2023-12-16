import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Linux and macOS
    else:
        _ = os.system('clear')
