name=22
if name=='khan':
	print('logging to this page')
else:
	print('this page is not logging')
print('this page is loggging')
name='ali'
if name=='ali':
	print('this name is ali')
else:
	print('this name is not ali')
print('this code will be not executed')

if name=='harry':
	print('hello harry')
if password=='code':
	print('accesed code with harry')
else:
	print('wrong password')
name = 'sharda'
if name== 'sharda':
	print('this is the nmae is printed')
else:
	print('this is not use name')

name ='khan'
if name=='jan':
	print('this is the name code')
else age<5:
	print('this code is not excuted')

spam=0
if spam<5:
	print('this code will be executed')
	spam=spam+1
print(spam)

spam=0
while spam<5:
	print('hello my name is sufyab')
	spam=spam+1

i=1
while i<=10:
	print(i,'my name is ali')
	i=i+1
print(i)

i=10
while i>=1:
	print(i,'hello my name is sufyab')
	i=i-1
print(i)


name=''
while name != 'your name':
	print('please type your name: ')
	name=input()
print('thank your ')

name=''
while name!='you name':
	print('what is your name')
	name=input()
print('thank you')
while True:
	print('please type your name')
	name=input()
	if name=='your name':
		break
print('thank you')

while True:
	print('what is your name:')
	name =input()
	if name=='sufyan':
		break
print('hello my name is sufyan')

number=0
for a in range(10):
	number=a+1
	if number==5:
		break
	print(number)
print('out of the code')

number=0
for code in range(30):
	number=code+1
	if number==7:
		continue
	print(number)
print('out of there code will be execute')
number=0
for i in range(10):
	number=i+1
	if number==8:
		continue
	print(number)
print('out of the code')
number=0
for i in range(44):
	number=i+1
	if number==8:
		continue
	print(number)
print('this code will execute')
while True:
	print('who are you?')
	name=input()
	if name!='joe':
		continue
	print('hello,joe.what is password?(it is a fish.)')
	password=input()
	if password=='swordfish':
		break
print('Accesss granted.')
while True:
	print('what is your name:')
	name=input()
	if name!='sufyan':
		continue
	print('hello frind this is my first code')
	password=input()
	if password=='111':
		break
print('access the all code')
while True:
	print('who are you:')

	name=input()

	if name=='khan':
		continue
	print('this code will be explanne')
	password=input()
	if password=='ali':
		break
print('access the all code')

 

print("hello world")
name=input('what is your name:')
print(f'hello,{name}!nice to meet you')

name =input('what is your name:')
print(f"my name is {name}")


name=input('what is your name?')
if name=='Alice'or name=='Bob':
	print(f"Hello my name is {name}! you Good luck")
else:
	print('sorry yor are not code alice and bob')

n=int(input("Enter a number :"))
sum_of_number=sum(range(1,n+1))
print(f'the sum of number form 1 to {n}is :{sum_of_number}')

n=int(input("Enter a number (n):"))
sum_of_multipul=sum(x for x in range(1,n+1) if x%3==0 or x%5==0)
print(f'the sum of multiple of three or five form 1  to {n} is:{sum_of_multipul}')

while True:

	print('Who are you?')

	name = input()
 	if name != 'Joe':
		continue
	print('Hello, Joe. What is the password? (It is a fish.)')
	password = input()
	if password == 'swordfish':
		break
 print('Access granted.') 
while True:
	print('who are you:')
	name=input()
	if name !='ali':
		continue
	print('this code will execute ')
	password=input()
	if password=='jeo':
		break
	print('where this source code')
print('this code will end')
count=0
while (count<3):
	count=count+1
	print(count,'hello world')
while True:
	try:
		age=int(input('Enter your age:'))
		break
	except ValueError:
		print('Invalid input,please enter a valid input')
if age < 18:
	print('yor are a minor')
else:
	print('you are adault')
while True:
	try:
		age =int(input('Enter your agge:'))
		break
	except ValueError:
		print('the input is invalid')
if age <18:
	print('this is my age is valuid')
else:
	print('this age is not valuid')

i= 0
a='greekforgreek'
while i < len(a):
	if a[i] == 'e' or a[i] == 's':
		i +=1
		continue
	print('Current Letter:',a[i])
	i+=1

i = 0
a = 'geeksforgeeks'
  
while i < len(a): 
    if a[i] == 'e' or a[i] == 's': 
        i += 1
        continue
          
    print('Current Letter :', a[i]) 
    i += 1



print('My name is')
for i in range(5):
 print('Jimmy Five Times (' + str(i) + ')')
for n in range(10):
	print(n)
for n in range(1,6,3):
	print(n)
for a in range(1,11):
	print('2*',a,'=',2*a)
for i in range(5):
	print('sufyan('+str(i) +')')
	print('sufyan is my best frind(' +str(i) +')')
total=0
for num in range(10):
	total=total+num
	print(total)
for b in range(1,11):
	print('3*',b,'=',3*b)
for a in range(10,-4,-1):
	print(a)














