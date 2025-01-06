# We make lambda Function
# Lambda (Anonymous) Functions: Functions defined without a name, typically used for short, simple operations.
add=lambda a,b:a+b
Sub=lambda a,b:a-b
mul=lambda a,b:a*b
Divied=lambda a,b:a//b
Modul=lambda a,b:a%b
Square=lambda a:a*2
x=int(input("Enter a value:-"))
y=int(input("Enter a value:-"))
print("Addition:-",add(x,y))
print("Substracition:-",Sub(x,y))
print("Multipication:-",mul(x,y))
print("Division:-",Divied(x,y))
print("Mouduls:-",Modul(x,y))
print("Square of First value:-",Square(x))