foo = 'Please read the source code to understand the use of this program\n\n'

print(foo.upper())

print("Enter yes or no:")
answer = input()

if answer.lower() == 'yes':
    print('you said yes!')
elif answer.lower() == 'no':
    print('you said no!')

print('\nEnter a word in full-caps or full-lowercaps')
caps = input()

if caps.isupper():
    print("That was fully upper")
elif caps.islower():
    print("That was fully lower")
else:
    print('Not sure about this one\n')

#Other Functions Include, isalpha(), isalnum(), isdecimal(), isspace() and istitle()

print("Write a sentence that starts with hello")

hello = input()

if hello.startswith('hello'):
    print("nice")
else:
    print("nvm then")

join = ','.join(['cats', 'dogs'])

print("Hello World".split("e"))

print("This had a lot of asterisks in it!".ljust(50, '*'))

print("or use the center function!".center(50, '-'))

strip = "        this sentence has been stripped of all whitespaces at the beggining"

print(strip.strip()) #different varients include lstrip and rstrip

print("something was replaced!".replace('a', '0'))



