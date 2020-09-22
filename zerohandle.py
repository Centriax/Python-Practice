import sys

def main():

    x = int(input("Number Please: "))
    y = int(input("Another number please: "))

    try:
        return x / y
    except ZeroDivisionError:
        print("Unable to Divide by Zero, Quitting...")
        sys.exit()

print(main())
