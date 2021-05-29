# row = int(input('Enter number of rows required: '))

# for i in range(row,0,-1):
#     for j in range(row-i):
#         print(' ', end='') 
    
#     for j in range(2*i-1):
#         print('*',end='') 
#     print()



s = 9  
int = 1
m = (2 * s) - 1 
for i in range(1, s):  
    for j in range(1, m):  
        print(end=" ")  
    m = m - 1  
    for j in range(i+1 , 1 , -1):   
        print(int, end=' ')  
        int += 1  
    print()  