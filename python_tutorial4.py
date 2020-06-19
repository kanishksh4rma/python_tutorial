# advanced operators
# and or not in 

# program to distribute sweet among kids but not for kids older than 15. Nor for mikkel & jonas.
name = input('Enter name : ')
age = int(input('Enter age : '))

if age <= 15 and not(name == 'mikkel' or name=='jonas'):

    print('You can eat sweets.')

else:
    print('You cant eat sweets !')