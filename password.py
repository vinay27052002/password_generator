import string  
import random 
s1=string.ascii_lowercase 
s2=string.ascii_uppercase 
s3=string.digits
s4=string.punctuation
l=int(input("enter length of string "))
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
password='' 
 #print(s)
random.shuffle(s)
 # print(s)

password=password.join(s[0:l])
print(password)