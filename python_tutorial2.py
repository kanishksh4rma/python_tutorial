# marksheet count

name = input('Enter your name : ')

sub1 = int(input('Enter your marks in sub1 : '))
sub2 = int(input('Enter your marks in sub2 : '))
sub3 = int(input('Enter your marks in sub3 : '))

total = ((sub1+sub2+sub3)//3)
print(name, 'you got ',total, '%')

