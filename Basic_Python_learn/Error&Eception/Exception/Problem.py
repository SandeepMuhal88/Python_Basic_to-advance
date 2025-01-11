# try:
#     risky_code()
# except SomeException:
#     handle_code()


try:
    Value=int(input("Enter a number:-"))
    num=int(input("Enter a number:-"))
    result=Value/num
    print("Division in there program",result)
except ValueError:
     print("Please entered integer value not string form and floating and Boolean@##")
except ZeroDivisionError:
      print("Cannot divide by zero!")
      print("Sun bhai ye division posible nhi because:- you entered Zero!!")