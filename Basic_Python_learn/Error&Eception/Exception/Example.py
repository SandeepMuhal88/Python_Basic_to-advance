# try:
#     name=int(input("Enter your name "))
#     print(name)
# except Exception as e:
#     print(f"An error occured:{e}")

try:
    print(10 / 0)
except Exception as e:
    print(f"An error occurred: {e}")


# 5. Using else and finally