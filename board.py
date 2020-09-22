
board = {'top-L' : 'X', 'top-M': 'X', 'top-R': 'X', 'middle-L': ' ', 'middle-M': ' ', 'middle-R':' ', 'bottom-L':' ', 'bottom-M': ' ', 'bottom-R':' '}

def printBoard():
    print(f"{board['top-L']}|{board['top-M']}|{board['top-R']}")
    print('-----')
    print(f"{board['middle-L']}|{board['middle-M']}|{board['middle-R']}")
    print('-----')
    print(f"{board['bottom-L']}|{board['bottom-M']}|{board['bottom-R']}")


printBoard()