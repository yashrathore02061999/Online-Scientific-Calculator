import Calc1 as c
'''
Here we have a module or python pgm called Calc1.py. We have imported the module in our pgm Calculator_Main.py. And we have given
the name for the Calc1 module as c in this pgm.

This is our pgm which contains main() function. So we have to run this pgm.
'''


calculator1=c.Calculator(0.0,0.0)
'''
in above statement we have created object of Calculator class from Calc1 module which is renamed as c in this pgm. We have passed
input values 0.0 and 0.0 into parameters x and y of the construcyor i.e. init() method of the Calculator class

calculator1 is the object of Calculator class.

'''

while(True):
    option=int(input("\n Enter your choice....1.Addition  2. Subtraction   3. Division  4. Remainder   5. Quotient  6. Exponentiation/Power   7. Absolute value of integer   8. Absolute value for floating number    9. GCD of 2 numbers   10. LCMof 2 numbers    11. Factorial    12. Square root   13. Floor   14. Ceiling   15. Truncate   16. Degree to radians   17. Radians to degrees  18. Sin  19. Cos 20. Tan      21. multiplication   22. exit"))
    if(option==1):
        print("\n The addition is ",calculator1.add())

    elif (option == 2):
        print("\n The subtraction is",calculator1.sub())


    elif (option == 3):
        print(calculator1.div())

    elif (option == 4):
        print(calculator1.rem())


    elif (option == 5):
        print(calculator1.quotient())


    elif (option == 6):
        print(calculator1.exp())

    elif (option == 7):
        print(calculator1.abs1())




    elif (option == 8):
        print(calculator1.abs2())


    elif (option == 9):
        print(calculator1.gcd1())

    elif (option == 10):
        print(calculator1.lcm1())

    elif (option == 11):
        print(calculator1.factorial1())

    elif (option == 12):
        print(calculator1.sqrt())

    elif (option == 13):
        print(calculator1.floor1())

    elif (option == 14):
        print(calculator1.ceil1())

    elif (option == 15):
        print(calculator1.trunc1())

    elif (option == 16):
        print(calculator1.degrees1())

    elif (option == 17):
        print(calculator1.degrees2())

    elif (option == 18):
        print(calculator1.sin1())

    elif (option == 19):
        print(calculator1.cos1())

    elif (option == 20):
        print(calculator1.tan1())

    elif (option == 21):
        print(calculator1.mul())

    else:
        break












