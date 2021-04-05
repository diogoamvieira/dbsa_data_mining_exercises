"""
3. Create a function that:
a. Receives an integer number
b. Returns true if the given number is palindromic (eg.: 7, 77, 121,3443, 5341435).
"""

n = input('Enter a number: ')

def is_palindromic(n): 
    while True:
        try:
            value = int(n)
            if n == str(n)[::-1]:
                print('The number is palindromic!')
            else:
                print('The number is NOT palindromic!')
            break
        except:
            print('That number is not valid. Please try again.')
            n = input('Enter a number: ')
            
            
is_palindromic(n)