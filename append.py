names = ['John', 'Jack', 'Jill']

print("This list has names:")
for i in range(len(names)):
    print(str(names[i]))

print()
print("Enter your name to add to the list:")
name = input()

names.append(name)
print()

print("This list now has names: ")
for i in range(len(names)):
    print(str(names[i]))

