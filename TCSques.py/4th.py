# #### Bank machine 


# print("****************************************************************************")
# print("*                   Welcome to PNB Bank Gwalior                            *")
# print("****************************************************************************")
# restart=('yes')
# chances = 3
# balance = 10000
# while chances >= 0:
#     pin = int(input('Please Enter Your 4 Digit Pin: '))
#     if pin == (1234):
#         print('You entered your pin Correctly\n')
#         while restart not in ('n','NO','no','N'):
#             print('Please Press 1 For Your Balance enquiry \n')
#             print('Please Press 2 To Make a Withdrawl \n')
#             print('Please Press 3 For balance Pay in \n')
#             print('Please Press 4 To Return Card \n')
#             option = int(input('What Would you like to choose?'))
#             if option == 1:
#                 print('Your Balance is now',balance,'\n')
#                 restart = input('Would You you like to go back? ')
#                 if restart in ('n','NO','no','N'):
#                     print('Thank You')
#                     break
#             elif option == 2:
#                 option2 = ('yes')
#                 withdrawl = float(input('How Much Would you like to withdraw? \n'))
#                 if withdrawl in [100, 200, 500, 1000, 2000, 10000]:
#                     balance = balance - withdrawl
#                     print ('\nYour Balance is now',balance)
#                     restart = input('Would You you like to go back? ')
#                     if restart in ('n','NO','no','N'):
#                         print('Thank You')
#                         break
#                 elif withdrawl != [100, 200, 500, 1000, 2000, 10000]:
#                     print('Invalid Amount, Please Re-try\n')
#                     restart = ('yes')
#                 elif withdrawl == 1:
#                     withdrawl = float(input('Please Enter Desired amount:'))    

#             elif option == 3:
#                 Pay_in = float(input('How Much Would You Like To Pay In? '))
#                 balance = balance + Pay_in
#                 print ('\nYour Balance is now',balance)
#                 restart = input('Would You you like to go back? ')
#                 if restart in ('n','NO','no','N'):
#                     print('Thank You')
#                     break
#             elif option == 4:
#                 print('Please wait while your card is Returned...\n')
#                 print('Thank you for your service')
#                 break
#             else:
#                 print('Please Enter a correct number. \n')
#                 restart = ('yes')
#     elif pin != ('1234'):
#         print('Incorrect Password')
#         chances = chances - 1
#         if chances == 0:
#             print('\n No more tries')
#             break
