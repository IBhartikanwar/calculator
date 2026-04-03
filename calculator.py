num1=int(input("enter the first no :"))
num2=int(input("enter the second no :"))
more=0
while(more !="n") : 
 operator =input("enter a operation to be performed among +,-,*,/,% : ")
 if operator == "+":
  print("sum of numbers is : ",num1+num2)
 if operator == "-":
  print("difference of numbers is : ",num1-num2)
 if operator == "*":
  print("product of numbers is : ",num1*num2)
 if operator == "/":
  if num2!=0 :
   print("division of numbers is : ",num1//num2)
  else :
   print("divide by zero is not allowed")
 if operator == "%":
  print("modulus of numbers is : ",num1%num2)
 else :
  print(" This operation does not exist here")
 print("want to perform more operations...y/n")
 more=input()
 if more=="n":
  break;
