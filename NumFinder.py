#!/usr/bin/env python3

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print("Input:")
message = input()

print("\nSearching for Numbers...\n")

foundNumber = False

for i in range(len(message)):
    load = message[i:i+12]
    if isPhoneNumber(load):
        print(f"Phone Number {load} found!")
        foundNumber = True
if not foundNumber:
    print("Phone number was not found.")
    
