hometown = 'Memorial'
x = 298784

# Varaibles #
j = 5 
l = 10 
print (j+l)

z= j+l 
print (z)

t= q= r= s= 'education'

#Data Types#
x = ["apple", "banana", "cherry"] 
y = ("apple", "banana", "cherry")
f = False
g = 'covid-19'

type (x)
type(y)
type(f)
type(g)

#If - Else and Scope#
x = 0
j = 3

def funky(arg1, arg2):
	global x 
	x = 1
	global j 
	j = 5
	if arg1 > arg2:
		print('arg1 is greater than arg2')
	else:
		print('arg1 is not greater than arg2')
	print(j)

funky(x, j)

print(x)
print(j)
## The out put should be 1 and 5 but becasue they are local variables in  the function they are not printed 
#when the function ends. So I made them global variables so that they print out at the end #

#Iterations#
lunches = ['burger','apple','soba','chahan']

for x in lunches:
	print (x)
	if x == 'apple':
		break
