a = int(input("what's your percentage:\n"))

if a <= 30:
    print("You failed , better luck next time")
elif a > 30 and a <= 50:
    print("You have scored 3rd divison , practice more")
elif a > 50 and a <= 80:
    print("You have scored 2nd division , good job")
elif a > 80 and a <= 100:
    print("You have scored 1st division , Excellent work \n Your interview timing will be 1 pm to 2 pm \n All the best!!")
else :
    print("You have not attempted your exam , You are disqualified")