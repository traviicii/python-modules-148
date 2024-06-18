import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def d():
    '''
    This function simply prints a dividing line to the terminal
    '''
    print('=' * 75)

def get_num():
    while True:
        try:
            x = int(input("Please enter your first number "))
            y = int(input("Please enter the second number "))
        except ValueError:
            print("I know what you just tried to do. Please enter a number!")
        except Exception as e:
            print("Oof, looks like something must've gone wrong here...")
            print(e)
        else:
            return (x, y)
        

if __name__ == "__main__":
   print(get_num())