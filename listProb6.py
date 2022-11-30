def ispalindrome(s):
   i=len(s)-1
   r=[]
   while i>=0:
       r.append(s[i])
       i=i-1
       
       
   r=''.join(r)
   if r==s:
         return True
   else:
         return False

x=input('enter a string')
t=ispalindrome(x)

if t==True:
    print("palindrome")
else:
    print("not a palindrome string")
