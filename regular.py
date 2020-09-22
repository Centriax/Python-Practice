import re
import pprint

print("Input:")
message = input()

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

match = phoneNumRegex.search(message)

print("Phone Number: ", end='')
print(match.group(0), end='')
print(', with area code: ', end='')
print(match.group(1))



