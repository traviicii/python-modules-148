# Main functionality
import operations as op # import with alias
from operations import add, div # Importing specific functions by name

def main():
    print('''
 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗      █████╗ ██████╗ ██████╗ 
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗
██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝    ███████║██████╔╝██████╔╝
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗    ██╔══██║██╔═══╝ ██╔═══╝ 
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║    ██║  ██║██║     ██║     
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝     
                                                                                                                                                                                                                                                                          
''')
    while True:
        choice = input('''
What action would you like to perform? 
    1 - Addition
    2 - Subtraction
    3 - Multiplication
    4 - Division
    5 - Square Root
    6 - Quit
''')
        if choice == '1':
            x, y, ans = add() # addition
            print(f"The sum of {x} and {y} = {ans}!")
        elif choice == '2':
            x, y, ans = op.sub() # subtraction
            print(f"The difference of {x} and {y} = {ans}!")
        elif choice == '3':
            x, y, ans = op.mult() # Multiplication
            print(f"The product of {x} and {y} = {ans}!")
        elif choice == '4':
            x, y, ans = div() # Division
            print(f"The quotient of {x} and {y} = {ans}!")
        elif choice == '5':
            x, ans = op.root() # Square root
            print(f"The square root of {x} = {ans}!")
        elif choice == '6':
            print('''

   ▄▄▄▄▀ ▄  █ ██      ▄   █  █▀  ▄▄▄▄▄       ██▄     ▄   ██▄   ▄███▄     ▄ 
▀▀▀ █   █   █ █ █      █  █▄█   █     ▀▄     █  █     █  █  █  █▀   ▀   █  
    █   ██▀▀█ █▄▄█ ██   █ █▀▄ ▄  ▀▀▀▀▄       █   █ █   █ █   █ ██▄▄    █   
   █    █   █ █  █ █ █  █ █  █ ▀▄▄▄▄▀        █  █  █   █ █  █  █▄   ▄▀ █   
  ▀        █     █ █  █ █   █                ███▀  █▄ ▄█ ███▀  ▀███▀       
          ▀     █  █   ██  ▀                        ▀▀▀                ▀   
               ▀                                                           ''')
            break

if __name__ == "__main__":
    main()