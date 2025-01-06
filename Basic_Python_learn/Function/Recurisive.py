# Recursive Functions: Functions that call themselves to solve smaller instances of a problem.
# Make function to calculate Factoriyal 

def factoriyal(n):
    fact=1
    if(n<0):
        print("Negative number factoriyal not defined:(")
    elif(n==0):
        print("Factoryal",n)
    else:
        while(n!=1):
            fact=fact*n
            n=n-1
        print(f"{n} Factoriyal of you entered number:-",fact)

def main():
    while True:
        print("\nWelcome to my program(*_*)")
        print("To calculate facotiyal number please prees 1:-")
        print("Exit to the program prees 2:-",end="\n")
        
        choice=int(input("Enter your choce:-"))
        if choice==1:
            n=int(input("Enter number to calculate factoriyal:-"))
            factoriyal(n)
            continue
        elif choice==2:
            print("Thank you have nice day😁😁")
            break
        else:
            print("Invaid number:🤬🤬🤬😡")


main()


