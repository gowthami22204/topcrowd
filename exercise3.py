[Wednesday 10:59 AM] Anil Kumar Nahak
1.what is a variable in python and describe the role of variable in python memory management?

variable in python refer to store any value to a perticular variable ,which will give the type of data stored in a perticular virable
in python variable  is stored in stack memory and the  data given to a perticular variable  is  stored in "heap memory"
in python their are two memory i.e stack and heap memory

for ex:
    a=30
    here in the above ex "a" ia variable and 30 is the data given to a perticular
    variable
    type refers to type of data stored in a variable
    type(a)
    int type
================================================================================================================================    
2.what are the advantages and disadvantages of type casting?
type casting:converting of one data type into another is called as type casting.
their are 2 type of converting explict and implicit
exlict type casting:which is done by the programmer while writing the code.
implict tye casting:which is done during the execution of the program.

            Advantages                  disadvantages
1.it is easy to convert one type of       1.Their is a lot of memory wastage
data into another while programming     in type cating

2.the type convertion can be done         2.its take lot of time for exercution
iternally depending upon the input
given by the user

==============================================================================================================================
3.what is the difference between while loop and for loop?
while loop:In  while loop followed by the set of statement and it will be executed till the block of code or
the given condition is "true".here in while loop we can give more than 1 condition followed by "and"
for ex: while statement:
              condition:1
              condition:2

for loop:for loop is used to execute  "range"   of elements in the given range.
it fallow sequencial type of execution of program.
for ex:for i in range (0,10)

=============================================================================================================================
4.write 5 string method with example?
string.upper()
string.lower()
l.strip()
r'strip()
is upper()
is.lower()

x="hello"
print(x.isupper())
output:False

x="HelloS"
print(x[0].isupper())
output:True

str="gowthami"
print(str.upper())
print(str.lower())

#output:
GOWTHAMI
gowthami
====================================================================================================================
5.write the Precedence rule of python with example?

In python  the paranthesis plays a key role.it fallow the same rule just what we fallow in mathematics(BODMUAS method).
Bracket of division multilication addition and subtraction.
for example:
a=30
b=12
c=2
d=10
print(a*(c+d)/b)
    
