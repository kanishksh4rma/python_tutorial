# if else
# Driving lisence

name = input('Enter your name : ')
age = int(input('Enter your age : '))
print('====================')

if age >= 18 and age < 75 :
    print(name,' You can drive !')

elif age == 0 :
    print('WARNING : Age can\'t be Zero (0) !!' )

else:
    print('You can\'t drive ')

print('====================')

# end of the program