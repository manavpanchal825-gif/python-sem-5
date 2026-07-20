try :
    a = 10/0
    print (a)
except ArithmeticError:
    print("Arithmetic Exception Raised.")
else :
    print("Success")
    