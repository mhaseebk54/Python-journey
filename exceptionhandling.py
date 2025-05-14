try :
    number = 10
    number / 0
    print("Result",number)
except :
    print("Can't divided by 0")    



try :
    file = open("hello.txt", "r")

except:
    print("File doesn't exists")

try :
   val = int(input("Enter a Value : "))
   print("You Input this value",val)
except :
    print("You Enter invalid value")   

try :
    a = int (input("enter 1 value : "))
    b = int (input("enter 2 value : "))
    print(a+b)

except :
    print("Invalid Numerical Value")


