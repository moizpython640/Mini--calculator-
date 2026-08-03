print("==mini calculator==")
num1 = float(input("Enter your first number: "))
operatore = input("Enter operator( +, *, -, / ): ")
num2 = float (input("Enter your second number: "))
if operatore == "+":
    print("Answer =", num1 + num2)
elif operatore == "-":
	print("Answer =", num1 - num2)   
elif operatore == "*":
	print("Answer =", num1 * num2)
elif operatore == "/":
    if num2   != 0:	  
          print("Answer =", num1 / num2)
    else:
             print("error:  cannot divide by zero!")
else:
    	print("invalid operation")
	
			