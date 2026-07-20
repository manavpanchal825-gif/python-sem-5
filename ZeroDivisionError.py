try:
    num1, num2 = eval(input("Enter Two Numbers,Seprated By A Comma:"))
    result = num1 / num2
    print("Result Is", result)

except ZeroDivisionError:
    print("Divisiojn by Zero Is Error !!!!")

except SyntaxError:
    print("comma Is missing Enter number Seprated by Comma Like This 1,2")

except:
    print("Wrong Input")

else:
    print("No Exception")

finally:
    print("Thius Will Execute No Matter What")
