name = input()
python
name
'python'

name =input("enter the name: ")
enter the name: Jahanavi
name
'Jahanavi'

age =input("enter the age:")
enter the age:22
age
'22'

age = int(input("enter the age:"))
enter the age:22
age
22
type(age)
<class 'int'>

price = input("enter the price:")
enter the price:2000.58
price
'2000.58'

price = float(input("enter the price:"))
enter the price:2000.8
price
2000.8
type(price)
<class 'float'>

'Jahanavi Kavya Asritha Hema'
'Jahanavi Kavya Asritha Hema'

'Jahanavi Kavya Asritha Hema'.split()
['Jahanavi', 'Kavya', 'Asritha', 'Hema']

'Jahanavi Kavya Asritha Hema'.split(',')
['Jahanavi Kavya Asritha Hema']

'Jahanavi, Kavya, Asritha, Hema'.split(',')
['Jahanavi', ' Kavya', ' Asritha', ' Hema']

names =input("enter the names: ")
enter the names: Jahanavi Asritha kavya hema
names
'Jahanavi Asritha kavya hema'

names =input("enter the names: ").split()
enter the names: Jahanavi Asritha kavya hema
names
['Jahanavi', 'Asritha', 'kavya', 'hema']

numbers =input("enter the numbers:").split()
enter the numbers:1 2 3 4 5 6 7 
numbers
['1', '2', '3', '4', '5', '6', '7']

numbers =list(map(int,input("enter the numbers:").split()))
enter the numbers:1 2 3 4 5
numbers
[1, 2, 3, 4, 5]

numbers =list(map(float,input("enter the numbers:").split()))
enter the numbers:8.9 32.4 8.22 9 6 
numbers
[8.9, 32.4, 8.22, 9.0, 6.0]
type(numbers)
<class 'list'>

numbers =tuple(map(int,input("enter the numbers:").split()))
enter the numbers:1 2 3 4 5
numbers
(1, 2, 3, 4, 5)
type(numbers)
<class 'tuple'>

numbers =tuple(map(float,input("enter the numbers:").split()))
enter the numbers:8.9 32.4 8.22 9 6
numbers
(8.9, 32.4, 8.22, 9.0, 6.0)

numbers =set(map(int,input("enter the numbers:").split()))
enter the numbers:2 3 4 5 7 8 
numbers
{2, 3, 4, 5, 7, 8}

numbers =set(map(float,input("enter the numbers:").split()))
enter the numbers:32.4 4.9 8.2 2.8
numbers
{32.4, 8.2, 2.8, 4.9}

d = eval(input("enter the input:"))
enter the input:{1:1,2:4,3:9,4:16}
d
{1: 1, 2: 4, 3: 9, 4: 16}

d=eval(input("enter the input:"))
enter the input:[1,2,3,4,5]
d
[1, 2, 3, 4, 5]

a,b,c=10,20,30
a
10
b
20
c
30
a=b=c=20
a
20
b
20
c
20

username,password = ['py','py123']
username
'py'
password
'py123'

username,password=input("enter the username and password:").split()
enter the username and password:Jahanavi Janu@123
username
'Jahanavi'
password
'Janu@123'

a,b,c=list(map(int,input("enter the sides:").split()))
enter the sides:8 9 6
a
8
b
9
c
6

a=10
b=8
a+b
18
a-b
2
a*b
80
a/b
1.25
a//b
1
a%b
2
a**2
100
b**2
64
a
10
b
8

a>b
True
a<b
False
a==b
False
a<=b
False
a>=b
True
a!=b
True

a=20
a=a+30
a
50
a+=10
a
60
a-=10
a
50
a=a*90
a
4500
a*=10
a=a/10
a
4500.0
a/=10
a
450.0

8%2==0 and 8%4==0
True
8%2==0 and 8%3==0
False
8%2==0 or 8%3==0
True
7%3==0
False
not 7%3==0
True
not 6%3==0
False

n='Jahanavi'
'J' in n
True
's' in n
False

l=[1,2,3,4]
4 in l
True
5 not in l
True

t=(1,3,8)
8 in t
True
7 in t
False

s={1,2,3,4,5,6}
7 in s
False
7 not in s
True

d={1:1,2:4,3:9}
1 in d
True
4 in d
False
3 in d
True
9 in d
False

a=[1,2,3,4,5,6]
b=[1,2,3,4,5,6]
a==b
True
a is b
False
c=a
c
[1, 2, 3, 4, 5, 6]
a==c
True
a is c
True
id(a)
1691356720072
id(b)
1691356720968
id(c)
1691356720072
a
[1, 2, 3, 4, 5, 6]
a.append(8)
a
[1, 2, 3, 4, 5, 6, 8]
a.append(9)
a
[1, 2, 3, 4, 5, 6, 8, 9]
id(a)
1691356720072

s='python'
id(s)
1691355825520
s+='lang'
s
'pythonlang'
id(s)
1691354805488




1-0001
2-0010
3-0011
4-0100
5-0101
6-0110
7-0111
8-1000
9-1001
10-1010
11-1011
12-1100
13-1101
14-1110
15-1111

& | ^ ~ << >>

10&11
10

15&1
1

7^8
15

12^11
7

~2
-3

~89
-90

10<<2
40

2>>1
1

