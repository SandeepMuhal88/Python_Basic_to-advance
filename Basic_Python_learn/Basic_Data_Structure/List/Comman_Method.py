"""Common List Methods
1. Adding Items
.append(item): Adds an item to the end of the list.
.insert(index, item): Inserts an item at a specific index.
.extend(iterable): Adds multiple items (from another list or iterable) to the end."""


l1=['Banana',56,6,41,100]
l1.append(50000)
print(l1)

# Insert MEthodl
l1.insert(5,"Insert method")
print(l1)


# Extend MEthos
l1.extend(["Sandeep","Muhal"])
print(l1)



"""2. Removing Items
.remove(item): Removes the first occurrence of the specified item.
.pop(index): Removes and returns the item at the given index (default: last item).
.clear(): Removes all items from the list."""



l2=[40,2,0,52,0,6,3,1,41,52,63,'Apple','Banana','chery']
print(l2)
l2.remove('Banana')
print(l2)