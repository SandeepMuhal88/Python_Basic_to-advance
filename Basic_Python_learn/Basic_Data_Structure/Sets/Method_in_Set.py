s1={4,2,6,9,4}
s1.add(500)
s1.add(200)
s1.add(250)
s1.add(1000)
print(s1)
print(s1.remove(4))
# print(s1.remove(500))   #That vaule is not in set then remove method through key error
s2={4,2,6,9,4}
s2.add("Sandeep")
s2.add("Muhal")
s2.add("Ajmer")
s2.add("Rajasthan")
print(s2)
s2.discard("Sandeep")   #That vaule is not in set then discard method not given error
print(s2)