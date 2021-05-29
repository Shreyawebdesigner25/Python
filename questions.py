# write a program to print multiplication table of a
# given number using for loop
# num1 = int(input("enter an integer:-"))
# for i in range(1,11):
#     print(f"{num1*i}") 


## write a program to print from 1 to n

# n = int(input("pic a number:-"))
# for i in range(1,(n+1)):
#     print(i)


## program to sum upto a number
# n = int(input(("enter a number"))
# sum = 0
# i = 1
# while(i<=n) :
#     sum = sum+i
#     i = i+1
# print("sum",sum)

##write a program to print the sum of square/cube from 1 to n

# n = int(input("enter a number:-"))
# sum = 0
# i = 2
# while(i<=n):
#     sum = sum+(i*i)
#     i = i+1
# print("sum of square", sum)

###write a program to print only even number between 1 to n

# n = int(input("enter a number:-"))
# i = 2
# while(i<=n):
#     if i%2 == 0:
#         print(i)
#     i = i+2

###write a program to find sum of even numbers from 1 to n

# n = int(input("enter a number:-"))
# i = 2
# sum = 0
# while 




#### sum of digits of given number
# i = int(input())
# sum = 0
# while (i>0):
#     sum = 




    ###sum of digits of squares

    # n = int(input())
    # sum = 0
    # for i in range(1,n+1):
    #     sum = sum + i**2
    #     print(sum)


###sum of cube
# n = int(input("Enter a number:-"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + (i*3)
#     i = i//10
#     print(sum)


###to check armstrong number

# i = int(input("enter number:-"))
# orig = i
# sum = 0
# while (i>0):
#     sum = sum + (i%10)*(i%10)*(i%10)
#     i = i//10
# if (orig==sum):
#     print("this is an armstrong number")
# else:
#     print("not armstrong")


#####product of digits of a number

# num = int(input("enter a number:-"))
# n = num
# product = 1
# while n != 0:
#     rem = n % 10
#     product = product * rem
#     n = n // 10
# print(product)


####reverse of a number

# number = int(input("Enter the integer number: "))  
# revs_number = 0  
# while (number > 0):  
#     remainder = number % 10  
#     revs_number = (revs_number * 10) + remainder  
#     number = number // 10  
# print("The reverse number is : {}".format(revs_number))  


### prime or not 
# num = int(input("enter a number:-"))
# if num > 1:
#     for i in range(2,int(num/2)+1):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
 
# else:
#     print(num, "is not a prime number")


####factorial of a given number

#### fibonaki series

# n = int(input("How many terms? "))
# count = 0
# n1 = 0
# n2 = 1

# if n <= 0:
#    print("Please enter a positive integer")
# elif n == 1:
#    print("Fibonacci sequence upto",n,":")
#    print(n1)
# else:
#    print("Fibonacci sequence:")
#    while count < n:
#        print(n1)
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count += 1

