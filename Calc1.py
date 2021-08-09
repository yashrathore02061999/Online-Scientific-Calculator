'''
implement a scientific calculator using classes and object. define your calculator class in 1 pgm and access it in another pgm.

'''

# // is the floor division which returns only integer part of division
'''
a**b is called as a raised to b or exponentiation operator.

Package is a predefined folder in the java system library. Package can also be called as a module in python which contains the definitions of many predefined classes and predefined functions in python. Suppose we want to use predefined functions or predefined classes in a package in python we need to write import statement.
import math
Using above statement we have imported all the predefined functions and classes whose definitions belong to math package. So now just by using dot operator on name of math package we can use any of the predefined functions or predefined classes in math package.

import math as m
here using above statement we have imported all predefined functions and classes in math package in our pgm but we are going to use name of the math package in our pgm as m. We can give any valid identifier name instead of m in the abovbe import statement. So now suppose we want to use any of the predefined functions or predefined classes of the math package in our pgm then after writing the above statement import math as m, we need to use dot operator on identifier name m to access predefined classes and predefined functions belonging to the math package.

from math import sqrt,factorial
now using above import statement on the math package name we can use only predefined functions like sqrt() and factorial() which we have mentioned in above import statement in our pgm.


ceil() is a predefined function in the math package

math.ceil(x) where x contains a floating value witha  decimal point returns the smallest integer value which is
greater than x
e.g. math.ceil(8.9) returns 9

math.floor(x) where x contains a floating value witha  decimal point returns the greatest integer value which is
smaller than x
e.g. math.floor(8.9) returns 8

math.trunc(x) where x contains a floating value witha  decimal point returns the an integer value after removing
the fractional part of the x value
e.g. math.trun(9.9) returns 9





'''

import math as m

'''
every member method of class must have first parameter as self which means currently executing object of the class i.e. object on which
we called the corr. member method.
In the below constructor i.e. init() , self.x and self.y are defining 2 instance data members for class Calculator. 
'''
class Calculator:
 def __init__(self,x,y):
  self.x=x
  self.y=y

 def add(self):
  self.x=int(input("\n Enter the 1st number to be added:"))
  self.y=int(input("\n Enter the 2nd number to be added:"))
  return (self.x+self.y)


 def sub(self):
  self.x=int(input("\n Enter the 1st number to be subtracted:"))
  self.y=int(input("\n Enter the 2nd number to be subtracted:"))
  return (self.x-self.y)

 def mul(self):
  self.x=int(input("\n Enter the 1st number to be multiplied:"))
  self.y=int(input("\n Enter the 2nd number to be multiplied:"))
  return (self.x*self.y)


 def div(self):
  self.x=int(input("\n Enter the dividend in the division operation:"))
  self.y=int(input("\n Enter the divisor in the division operation:"))
  return (self.x/self.y)

 def quotient(self):
  self.x=int(input("\n Enter the dividend in the division operation to find quotient:"))
  self.y=int(input("\n Enter the divisor in the division operation to find quotient:"))
  return (self.x//self.y)

 def rem(self):
  self.x=int(input("\n Enter the dividend in the division operation to find remainder:"))
  self.y=int(input("\n Enter the divisor in the division operation to find remainder:"))
  return (self.x%self.y)

 def exp(self):
  self.x=float(input("\n Enter the value of a for finding a raised to b:"))
  self.y=int(input("\n Enter the value of b for finding a raised to b:"))
  return (self.x**self.y)

 def sqrt(self):
  self.x=float(input("\n Enter the number for calculating square root:"))
  return (m.sqrt(self.x))

 def factorial1(self):
  self.x=int(input("\n Enter the number for calculating factorial:"))
  return (m.factorial(self.x))

 def abs1(self):
  self.x=int(input("\n Enter the integer number for calculating absolute value:"))
  return (abs(self.x))

 def abs2(self):
  self.x=float(input("\n Enter the float number for calculating absolute value:"))
  return (m.fabs(self.x))


 def ceil1(self):
  self.x=float(input("\n Enter the float number for calculating ceiling value:"))
  return (m.ceil(self.x))

 def floor1(self):
  self.x=float(input("\n Enter the float number for calculating floor value:"))
  return (m.floor(self.x))


 def trunc1(self):
  self.x=float(input("\n Enter the float number for calculating truncated value:"))
  return (m.trunc(self.x))



 def sin1(self):
  self.x=float(input("\n Enter the angle in radians for calculating sine value:"))
  return (m.sin(self.x))

 def cos1(self):
  self.x=float(input("\n Enter the angle in radians for calculating cosine value:"))
  return (m.cos(self.x))

 def tan1(self):
  self.x=float(input("\n Enter the angle in radians for calculating tan value:"))
  return (m.tan(self.x))


 def degrees2(self):
  self.x=float(input("\n Enter the angle in radians for calculating degrees:"))
  return (m.degrees(self.x))

 def degrees1(self):
     self.x = float(input("\n Enter the angle in degrees for calculating radians:"))
     return (m.radians(self.x))

 def log1(self):
     self.x = int(input("\n Enter the value for calculating log to base 10:"))
     return (m.log(self.x,10))

 def lcm1(self):
     self.x = int(input("\n Enter the 1st integer value for finding lcm:"))
     self.y = int(input("\n Enter the 2nd integer value for finding lcm:"))
     return (m.lcm(self.x,self.y))

 def gcd1(self):
     self.x = int(input("\n Enter the 1st integer value for finding gcd:"))
     self.y = int(input("\n Enter the 2nd integer value for finding gcd:"))
     return (m.gcd(self.x, self.y))







