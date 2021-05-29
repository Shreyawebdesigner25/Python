## no argument no return 
# def add():
#     a = int(input("enter 1st value"))
#     b = int(input("enter 2nd value"))
#     c=a+b
#     print(c)
# add()



## with argument no return 

# def add(a,b):
#     c=a+b
#     print(c)
# add(20,30)

## no argument with return 

# def add():
#     a = int(input("enter value:-"))
#     b = int(input("enter 2nd value:-"))
#     c = a+b
#     return c
# s = add()
# print(s)


### with argument with return 
# def add(a,b):
#     c = a+b
#     return c
# a = int(input("value 1"))
# b = int(input("value 2"))
# x = add(a,b)
# print(x)


# def add(a,b,c=12,d=6):        ###### its necessary to pass default argument of last element , otherwise it will show error
#     e = a+b+c+d
#     print(e)
# add(1,2,3,4)


# def factorial(num):
#     factorial=1
#     for i in range(1, num+1):
#         factorial=factorial*i
#     return factorial  
# number=int(input("Please enter any number to find factorial: "))
# result=factorial(number)
# print("The factorial of %d = %d"%(number,result))


# def fibonacci(n):  
#    if n <= 1:  
#        return n  
#    else:  
#        return(fibonacci(n-1) + fibonacci(n-2))   
# nterms = int(input("How many terms? "))  
# if nterms <= 0:  
#    print("Plese enter a positive integer")  
# else:  
#    print("Fibonacci sequence:")  
#    for i in range(nterms):  
#        print(fibonacci(i))  


#### sun of list elements

# list1 = [3,5,7,9,10,34,56,98,22]
# def sumOfList(list, size):
#    if (size == 0):
#      return 0
#    else:
#      return list[size - 1] + sumOfList(list, size - 1)
# total = sumOfList(list1, len(list1))
 
# print("Sum of all elements in given list: ", total)

## find greatest of three numbers 

# def largest(a, b, c):
#     if ((a > b) & (a >c)):
#         print("largest = " , a)
#     elif ((b > c) & (b > a)):
#         print("largest = " ,  b)
#     else:
#         print("largest = " , c)
#     return largest

# a = int(input())
# b = int(input())
# c = int(input())
# print(largest(a, b, c))

