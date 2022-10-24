# 1. Accept a char input from the user and display it on the console.
# print(input("Enter a character").strip()[0])
# 2. Accept two inputs from the user and output their sum.
# a,b =input("Enter two numbers").split()
# print("a:",a,"b:",b,"a+b",int(a)+float(b))
# 3. Write a program to find the simple interest.
"""
p,n,r =input("Enter the principal amount, interest rate and number of years").split()
si=int(p)*float(n)*float(r)/100
print("The interest rate of the amount {} at an interest rate of {} for {} years is: {} ".format(p,n,r,si))
"""
# 4. Write a program to check whether a student has passed or failed in a subject after he or she enters their mark
# (pass mark for a subject is 50 out of 100)
'''
def check(m):
    if 50<=m<=100:
        print("You have passed")
    else:
        print("You have failed")
mark = float(input("Enter your marks"))
check(mark)
'''
# 5. Write a program to show the grade obtained by a student after he/she enters their total mark percentage.
'''
# function to find the grade
def calculate():
    if mark>100:
        g = "0"
    elif mark>=90:
        g = "A"
    elif mark>=80:
        g = "B"
    elif mark>=70:
        g = "C"
    elif mark>=60:
        g = "D"
    elif mark>=50:
        g = "E"
    else:
        g = "Failed"
    return g
 # function to display the grade
def display(g):
    if g == "0":
        print("The mark you entered is wrong")
    else:
        print("Your grade is ",g)
mark = float(input("Enter your mark"))
display(calculate()
'''
# 6. Using the ‘switch case’ write a program to accept an input number from the user and output the day as follows.
"""
inp = {
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday',
    7: 'Saturday'
}
def day(i):
    if i in inp.keys():
        print(inp[i])
    else:
        print("You have entered the wrong input")
for key,value in inp.items():
    print("Enter {} for {}".format(key,value))
num = int(input())
day(num)
"""
# 7. Write a program to print the multiplication table of given numbers.
'''
def mul_table(i, l):
    if l<=10:
        print("{} X {} = {}".format(i,l,i*l))
        mul_table(i, l+1)
inp = int(input("Enter a number"))
for i in range(1,11):
    print(i," X ",inp," = ",i*inp)
# mul_table(inp,1)
'''
# 8. Write a program to find the sum of all the odd numbers for a given limit
'''
def sum(l):
    s=0
    for i in range(1,l+1,2):
        s+=i
    return s
inp = int(input("Enter the limit"))
print("Sum of odd numbers is: ",sum(inp))
'''
# 9. Write a program to print the following pattern (hint: use nested loop)
'''
def pattern(l):
    for i in range(1,l+1):
        for j in range(1,i+1):
            print(j, end="")
        print()
pattern(int(input("Enter the limit")))
'''
# 10. Write a program to interchange the values of two arrays.
'''
size=int(input("Enter the limit"))
print("Enter the values of array 1")
arr_first=[int(input()) for i in range(size)]
print("Enter the values of array 2")
arr_second=[int(input()) for i in range(size)]
temp=arr_first
arr_first=arr_second
arr_second=temp
print("Array 1:",arr_first)
print("Array 2:",arr_second)
'''
# 11. Write a program to find the number of even numbers in an array
'''
def find_even(array):
    c=0
    for i in array:
        if i%2==0:
            c+=1
    return c

size=int(input("Enter the limit"))
print("Enter the values of array ")
arr=[int(input()) for i in range(size)]
print("Number of even numbers in the given array is: ",find_even(arr))
'''
# 12. Write a program to sort an array in descending order
'''
def sort(a,s):
    for i in range(s):
        for j in range(i+1,s):
            if a[i] < a[j]:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    return a
# size=int(input("Enter the limit"))
print("Enter the values of array ")
ar=list(map(int, input().split(",")))
size=len(ar)
# arr=[int(input()) for i in range(size)]
print("The entered array is: ",ar)
print("Sorted array:",sort(ar,size))
'''
# 13. Write a program to identify whether a string is a palindrome or not
'''
def palindrome(v):
    r=s[::-1]
    print("{} is palindrome".format(v)) if v.casefold()==r.casefold() else print("{} is not palindrome".format(v))
i='y'
while i=='y':
    s=input("Enter a string ").strip()
    palindrome(s)
    i=input("Enter Y to continue ").lower().strip()
'''
# 14. Write a program to add to two dimensional arrays
'''
def add(a_first,a_second,row,col):
    sum = [[a_first[i][j]+a_second[i][j] for j in range(int(c))] for i in range(int(r))]
    print("Sum:",sum)
r, c =input("Enter the size ").split()
arr_first=[[int(input("Enter the ({},{}) element: ".format(i,j))) for j in range(int(c))] for i in range(int(r))]
arr_second=[[int(input("Enter the ({},{}) element: ".format(i,j))) for j in range(int(c))] for i in range(int(r))]
print("First Array:",arr_first)
print("Second Array:",arr_second)
add(arr_first,arr_second,r,c)
'''
# 15. Write a program to accept an array and display it on the console using functions
'''
def getArray(c,r):
    arr_first = [[int(input("Enter the ({},{}) element: ".format(i, j))) for j in range(int(c))] for i in range(int(r))]
    return arr_first
def displayArray(array):
    print(array)
def main():
    a=[]
    row, col = input("Enter the size ").split()
    a=getArray(row,col)
    displayArray(a)
main()
'''
# 16. Write a program to check whether a given number is prime or not
'''
num=int(input("Enter a number "))
flag=0
for e in range(2,num):
    if num%e==0:
        flag=1
        break
print("{} is prime".format(num)) if flag==0 else print("Entered number is not prime")
'''
# 17. Write a menu driven program to do the basic mathematical operations such as addition, subtraction, multiplication and division
# (hint: use if else ladder or switch)
'''
class A:

    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    def multiplication(self):
        return self.a*self.b
    def division(self):
        return self.a/self.b
    def subtraction(self):
        return self.a-self.b
obj = A(int(input("Enter a: ")),int(input("Enter b: ")))
choices={
    1: obj.addition(),
    2: obj.subtraction(),
    3: obj.multiplication(),
    4: obj.division()
}
ch='y'
while(ch=='y'):
    c=int(input("Enter \n1: Addition\n2: Subtraction \n3: Multiplication \n4: Division\n"))
    if c in choices.keys():
        print(choices[c])
    else:
        print("You have entered the wrong choice")
    ch=input("To continue press y: ")
'''
# 18. Grades are computed using a weighted average.
'''
def get_marks():
    print("Enter your marks for written test, Lab exams and Assignments respectively:")
    marks=[int(input()) for i in range(3)]
    score=((marks[0]*.70) +(marks[1]*.20) + (marks[2]*.10))
    return score

print("Grade of the student is",get_marks())
'''
# 21. Write a program to multiply the adjacent values of an array and store it in an another array.
'''
def multi(a,s):
    new_arr=[]
    for i in range(s-1):
        new_arr.append(a[i]*a[(i+1)])
    return new_arr
size=int(input("Enter the array limit"))
array=[int(input()) for i in range(size)]
print(multi(array,size))
'''
# 22. Write a program to add the values of two 2D arrays
'''
def getArray(r,c):
    array=[[int(input("Enter the ({},{}) element: ".format(i,j))) for j in range(int(c))] for i in range(int(r))]
    return array
def addArray(array_first,array_sec,r,c):
    array_first=[[array_first[i][j]+ array_sec[i][j] for j in range(int(c))] for i in range(int(r)) ]
    print(array_first)
def main():
    row, col = input("Enter the size ").split()
    arr_one=getArray(row,col)
    arr_two=getArray(row,col)
    addArray(arr_one,arr_two,row,col)
main()
'''
'''
try:
    c = int(input("input:"))
    c_n="".join(reversed(c))
    print(c_n)
except ValueError:
    print("Error")
'''
'''
a = "hi?"
print(a.find("i"))
'''
'''
test="hi"
def check_scope():
    def do_local():
        test="i am local"
    def do_nonlocal():
        nonlocal test
        test="i am non local"
    def do_global():
        global test
        test="i am global"
    test='i am function scope'
    print(do_local())
    print(test)
    # do_nonlocal()
    print(test)
    do_global()
    print(test)

# print(test)
check_scope()
# print(test)

# test = 'i am global'


# def check_scope():
#     def local_scope():
#         test ="i am local scope"
#     def nonlocal_scope():
#         nonlocal test
#         test = 'i am non local '
#     def global_scope():
#         global test
#         test = 'iam global '
#     test = 'iam function'
#     local_scope()
#     print(test)
#
#
# check_scope()
# test="hehe"
# def check_scope():
#     def do_local_scope():
#         test="hi local"
#         print(test)
# 
#     do_local_scope()
#     test="hi fn"
# 
# 
# check_scope()
'''
'''
class car: #car class
    def __init__(self,name,mileage,max_speed): #car constructor
        self.name=name
        self.mileage=mileage
        self.max_speed=max_speed
    def display(self): #display instance fn
        print("Name:"+self.name+"\nMileage:"+str(self.mileage)+"\nMax speed:"+str(self.max_speed))
tesla=car("tesla",70.00,90) #object creation
tesla.display() #display tesla object
'''
'''
import datetime
print(datetime.datetime.now().strftime("%d:%m:%Y"))
print(datetime.date.today().day)
print(datetime.date.today().month)
'''
'''
class A:
    a=10
    def my_fn(self,name):
        print(name)
print(A.a)
o=A()
o.my_fn("hi")
'''
'''
command=input().split(" ")
if(command[0]=='sort'):
    command.sort()
    print(command)
'''
'''
f=open("trial.py")
f.close()
f_new=open("file_trial.py","w")
f_new.write("Hi welcome")
f_new.close()
f_n=open("file_trial.py",'r')
print(f_n.read())
'''
'''
def make_printer(msg):

    msg = "hi there"

    def printer():
        print(msg)

    return printer


print(make_printer("Hello there"))
'''''
# myprinter()
# myprinter()
# myprinter()

def sq_numbers(n):
    for i in range(1, n + 1):
        yield i * i


a = sq_numbers(3)
print(sq_numbers(3))
print("The square of numbers 1,2,3 are : ")
print(next(a))
print(next(a))
print(next(a))