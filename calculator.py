#! /usr/bin/python

a = input("enter value of a :")
b = input("enter value of b :")
d = input("choose operation: \n 1.addition \n 2.subtraction \n 3.multiplication \n 4.division \n")
if d==1:
   c = a+b
   print (c) 
elif d==2:
    c = a-b
    print (c)
elif d==3:
    c = a*b
    print(c)
else :
    c = a/b
    print (c)
