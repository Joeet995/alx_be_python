 
def perform_operation(x, y, operation):
 if operation == "add":
  result = x + y
 elif operation == "subtract":
  result = x - y
 elif operation == "multiply":
  result = x * y
 elif operation == "divide":
  if y == 0 : print("can not divied by zero")
  result = x / y
 else: print("not a valid input")
 return result