try:
    num=int(input("Enter a number:-"))
    print(f"Square of:{num**2}")
except ValueError:
    print("Invalid Value entered!!")
else:
    print("Calculation was Succefully!!😴🤑🤑")
finally:
    print("Execution is commplete!!")
