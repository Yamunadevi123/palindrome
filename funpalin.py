def palindrome(a):
 temp=a
 rev=0   
 while(a> 0):
    rem=a%10
    rev=(rev*10)+rem
    a=a//10
 if(temp==rev):
    x="number is palindrome"
 else:
    x="number is not palindrome"
 return x
a=int(input("enter a number"))
x=palindrome(a)
print(x)
