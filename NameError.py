try :
    print(x)
except NameError:
    print("Variable X is Not Defined")
except :
    print("somethiong Else Went Wrong")
    