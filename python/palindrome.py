#WAP to check a no is palindrome or not .
n=int(input("Enter a no. "))
y=n # because value of n changed in loop
s=0
while(n!=0):
    r=n%10
    s=s*10+r  # loop
    n//=10
print(s)    

if y==s :
    print(" it is a palindrome")
else :
    print("not a palindrome")

# eg 121, 1221
   

