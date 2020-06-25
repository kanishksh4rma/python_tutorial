# for , while loops

size = int(input('Enter the size : '))

for i in range(1 , size+1):
    print(i,end=' ')

a = (1,2,3,4,5)

print(a)

for i in a :
    print(i,end=' ')

print()


# while loop

number = int(input('Enter the no : '))
i=1

while(i<=20):
    # print table of any number
    print(number,' x ',i,' = ',i*number)
    i += 1


# do-while

# Not available in python and is not neccesary either.