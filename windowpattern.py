max = int(input('Enter the input : '))
for i in range(max):
	if(i==0 or i==max-1 or i== max//2):
		print('* '*max,end='')
	else:
		print('*'+' '*(max-2)+'*'+' '*(max-2)+'*',end='')
	print()
