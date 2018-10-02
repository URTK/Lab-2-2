x,y = float(input('x = ')),float(input('y = '))

if (x>=1 and x<=7 and y>=1 and y<=7): # Входит в квадрат ?
	if (x+y>=5 and x+y<=11 and x-y>=-3 and x-y<=3): # Входит в ромб?
		print('True')
	else:
	    print('False')
else:
    print('False')

