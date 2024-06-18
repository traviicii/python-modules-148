from helper import get_num, clear
import math

def add():
    x, y = get_num()
    clear()
    return x, y, x + y

def sub():
    x, y = get_num()
    clear()
    return x, y, x - y

def mult():
    x, y = get_num()
    clear()
    return x, y, x * y

def root():
    try:
        x = int(input("what do you wanna find the square root of? "))
    except ValueError:
            print("I know what you just tried to do. Please enter a number!")
    clear()
    return x, math.sqrt(x)

def div():
    while True:
        x, y = get_num()
        try:
            quotient = x / y
        except ZeroDivisionError:
            print("Nope, no sir! Can't divide by zero! Try again!")
            continue
        except Exception as e:
            print(e)
        else:
            clear()
            return x, y, quotient

if __name__ == "__main__":
   print(div())