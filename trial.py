# Tuple1 = ('Geeks')
# n = 5
# print("\nTuple with a loop")
# for i in range(int(n)):
#     Tuple1 = (Tuple1,)
#     print(Tuple1)
#
# unpacking of tuple
# tup = (2,"w",5)
# a,b,c=tup
# print(a)
# print(b)
# print(c)
# asterisk for assigning rest of the elements to the tuple as  a list
# d=(3,4,5,2,3,4,6,)
# a,b,*c = d
# print(a)
# print(b)
# print(c)
# t=(1,2,3)
# print(type(t))
# s={1,2,3}
# print(type(s))
# Below list wil return false as all the elements are not true.
# list1 = [10, 20, 30, 40, 50, ]
# print(all(list1))
#
# # Below set will return true as the set is empty
# set1 = { }
# print(all(set1))
#
# # Below dictionary wil return true as all elements of the dictonary are true.
# dict1 = {1: "Ask", 2: "Python"}
# print(all(dict1))
# String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')
#
# Fset1 = frozenset(String)
# print("The FrozenSet is: ")
# print(Fset1)
# r,c=5,5
# print(str(r)+" "+str(c))
# Explicit function
# def digitSum(n):
#     dsum = 0
#     for ele in str(n):
#         dsum += int(ele)
#     return dsum
#
#
# # Initializing list
# List = [367, 111, 562, 945, 6726, 873]
#
# # Using the function on odd elements of the list
# newList = [digitSum(i) for i in List if i & 1]
# Displaying new list
# Python program to illustrate short hand if-else
# i = 10
# print(True) if i < 15 else print(False)
# looping using enumerate
# l=[1,4,5,6,7]
# for i in enumerate(l):
#     print(i)
# print("------------------------")
# for key,value in enumerate(l):
#     print(key,value)
# print("------------------------")
# for key, value in enumerate(l):
#     print(value)
# python code to demonstrate working of zip()

# # initializing list
# questions = ['name', 'colour', 'shape']
# answers = ['apple', 'red', 'a circle']
#
# # using zip() to combine two containers
# # and print values
# for question, answer in zip(questions, answers):
#     print('What is your {0}?  I am {1}.'.format(question, answer))
# python code to demonstrate working of items()

# d = {"geeks": "for", "only": "geeks"}
#
# # iteritems() is renamed to items() in python3
# # using items to print the dictionary key-value pair
# print("The key value pair using items is : ")
# for i, j in d.items():
# print(i, j)
# class A:
#
#     pass
# o=A( )
# # print(object.name)
class CSStudent:
    stream = 'cse'  # Class Variable

    def __init__(self, name, roll):
        self.name = name  # Instance Variable
        self.roll = roll  # Instance Variable


a = CSStudent("raju", 40)
b = CSStudent("ramu", 70)
CSStudent.stream = "hehe"

print(a.stream)
print(b.stream)