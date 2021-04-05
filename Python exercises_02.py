'''
Data Mining Exercises
'''

'''
2. Create a function that:
a. Receives a string:
b. print only the characters present at an even index number. (Eg.: ‘My string’ -> ‘M’, ‘ ’, ‘t’,’i’,’g’)
'''

my_string = str(input("Input text: "))

def print_even_index():
    for i in range(0, len(my_string)):
        if(i%2==0):
            print(my_string[i])
            
print_even_index()            

        




