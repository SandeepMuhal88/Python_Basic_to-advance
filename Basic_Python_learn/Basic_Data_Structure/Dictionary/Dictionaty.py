# dict={
#     "name":"Sandeep",
#     "age":21,
#     "marks":100
# }
# subject={
#     "Sub1":"Python",
#     "Sub2":"Machine Learning",
#     "Sub3":"Cloud Computing",
#     "Sub4":"Operating System"

# }
# print(dict)
# print(dict["name"])
# print(dict["age"])
# print(dict["marks"])
# print("Subject in Fifth Semester",subject)

# dict["name"]="Muhal"
# print(dict)
# # Method
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# #Operation
# del dict["age"]
# print(dict)

# # Dictionary can store multiple data types
# my_dict={
#     "name":"Sandeep",
#     "age":21,
#     "marks":100,
#     "subject":{
#         "Sub1":"Python",
#         "Sub2":"Machine Learning",
#         "Sub3":"Cloud Computing",
#         "Sub4":"Operating System"
#     }
# }
# print(my_dict)

# Dictionary have sub-dictionary
dict01={
    "name":"Rahul",
    "age":21,
    "marks":95,
    "Roll":45,
    "subject":{
        "Sub1":"Python",
        "Sub2":"Machine Learning",
        "Sub3":"Cloud Computing",
        "Sub4":"Operating System"
    }
}
print(dict01)
print(dict01["subject"]["Sub1"])