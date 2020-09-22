print("How old are you?")
age = input()

try:
    if int(age) < 40 and int(age) > 0:
        print("You are young!")
    elif int(age) <= 0:
        print("No.")
except ValueError:
    print("That was not a numerical digit.")
