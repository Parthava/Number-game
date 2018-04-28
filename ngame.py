import math
from random import randint

c=0
i=1

print('The game starts good luck \n')
while(i<20):
	r1=(randint(1, 10))
	r2=(randint(1, 10))
	if(r1==r2):
		c=c+1
	print(r1 , '\n')
	if(c>6):
		while True:
			r3=(randint(6, 10))
			if (r2!=r3):
				break
			r2=r3
	print(r2, '\n')
	input('Press Enter to continue \n')
	i=i+1
print('You won' , c , 'times')
print('You scored' , (c*500) , 'points')

