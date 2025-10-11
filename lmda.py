# a = lambda x : x**2
# print(a(2))

# a = lambda x : "Even" if x%2 ==0 else "Odd"
# print(a(3))

# b = lambda x: x[0] == "a" 
# print(b("apple"))



# def return_func(fn,l):
#     result = 0

#     for i in l:

#         if fn(i):
#             result = result + i
#     return result

# l = [23,11,3,52,68,23,41,9]

# x = lambda x : x%2==0
# y = lambda y : y%2!=0
# z = lambda z : z%3==0
# print(return_func(x,l))
# print(return_func(y,l))
# print(return_func(z,l))


#MAP FILTER REDUCE
# L = [1,2,4,5,6]
# # l = list(map(lambda x : x**2,L))
# l = list(map(lambda x : x%2==0 ,L))


# print(l)

# l1 = L+l
# print(l1)

students = [
    {
        "name": "Jacob Martin",
        "father_name": "Ros Martin",
        "address": "123 Hill Street"
    },
    {
        "name": "Angela Stevens",
        "father_name": "Robert Stevens",
        "address": "3 Upper Street London"
    },
    {
        "name": "Ricky Smart",
        "father_name": "William Smart",
        "address": "Unknown"
    }
]

# name_student = list(map(lambda student:student["name"],students))
# print(name_student)

l = [3,1,4,6,3,1,5]

abc = list(filter(lambda x: x>2 , l))

print(abc)


fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]

xyz = list(filter(lambda fruit: "e" in fruit ,fruits ))
print(xyz)

#REDUCE

import functools

list1 = [1,2,3,4,5]

red = functools.reduce(lambda x,y: x+y,list1)
print(red)

list2 = [23 , 34,21,55,12]
red1  = functools.reduce(lambda x,y : x if x>y else y, list2)
print(red1)

#LIST COMPREHENSION

lc1 = [1,2,3,4,5]

lc2 = [item*10 for item in lc1]
print(lc2)

lc3 = [i for i in range(10) if i%2==0]
print(lc3)

fruitslc= ["Apple", "Banana", "Cherry", "Mango", "Orange"]
lc4 = [fruit for fruit in fruits if fruit[0]=="O"]
print(lc4)

