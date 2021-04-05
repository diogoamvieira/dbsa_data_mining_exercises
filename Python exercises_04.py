"""
4. Using print(), format a decimal number to be displayed:
a. With 2 decimal places (eg.: 123.456 -> 123.46);
b. With 2 decimal places in exponential format (eg.: 123.456 ->1.23e+02).
"""

n = input('Enter a number: ')

while True:
    try:
        x = float(n)
        print('Number with 2 decimal places is', round(x,2))
        print('Number with 2 decimal places in exponential format is', '{:.2e}'.format(x))
        break
    except:
        print('That number is not valid. Please try again.')
        n = input('Enter a number: ')
