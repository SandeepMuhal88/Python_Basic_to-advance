"""Finding and Replacing:

.find(), .index(), .replace(), .startswith(), .endswith()"""

name=input("Enter your name:-")
print(name.find("A"))
Address="Rajsthan Is here and i am programer:-"
print(Address.find('here'))

print(Address.index('t'))

# Replace
print(Address.replace("Rajsthan", 'Gujrat'))
# Address can replace but string is ummutable properties so dont change in varible
print(Address)
print(Address.endswith('am'))
print(Address.startswith('Rajsthan'))


# Use splite
Address="Chhota narena Ajmer Rajasthan"
print(Address.split())
print(Address.split(','))
print(Address.split('a',2))
print(Address.split())