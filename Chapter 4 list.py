#list
friends = ["Apple","Orange",5,43.63,False,"Akash","Rohan"]
print(friends[0])
friends[0]= "Grapes"
print (friends[0:5])

a= "shrinath"
print(a[0:8])

# list methods
l1=[1,2,3,4,5,6]
l1.sort()
l1.reverse()
l1.insert(1,33333)
print(l1.pop(0))

value=l1.pop(2)
print(l1)
l1.remove(3)
print(l1)

lst = [1, 2, 3]
lst.append(4)
print(lst)  # Output: [1, 2, 3, 4]

lst = [1, 2, 3]
lst.extend([4, 5])
print(lst)  # Output: [1, 2, 3, 4, 5]

lst = [1, 2, 3]
index = lst.index(2)
print(index)  # Output: 1

lst = [1, 2, 2, 3]
count = lst.count(2)
print(count)  # Output: 2

lst = [1, 2, 3]
new_lst = lst.copy()
print(new_lst)  # Output: [1, 2, 3]

lst = [1, 2, 3]
lst.sort(reverse=True)
print(lst)  # Output: [3, 2, 1]

lst = [1, 2, 3]
print(len(lst))  # Output: 3

lst = [0, 1, 2]
print(any(lst))  # Output: True (because 1 and 2 are truthy)

lst = [1, 2, 3]
print(all(lst))  # Output: True (because all are truthy)



