print("HELLOWORLD")
a=2
b=3
result=a+b
print(result)
a=20#integer
print(a)
b=30
print(b)
print(type(a))
print(type(b))
a="manikanta"#String
print(a)
a=20
b=20
print(a==b)
a="nandamuri"
print(type(a))
#operators;
#1.arithmetic operator:
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a//b)
#2.assignment operator:
a=20
a+=10
print(a)
a-=20
print(a)
a*=20
print(a)
b=30
b/=20
print(b)
c=10
c//=10
print(c)
#3 comparison operator
a=10
b=20
print(a!=b)
print(a==b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
# 4 logical operator
a=2
b=3
print(a and b)
print(a>=2 and b<2)
print(a==2 or b==2)
print(not(a==2 and b==2))
# 5 identity operator
a=20
b=10
print(a is b)
print(a is not b)
# 6 membership operator
a=[1,2,3]
b=[1,2,3]
print(a in b)
print(a not in b)
# 7.BITWISE OPERATOR
a=20
b=20
print(a&b)
print(a|b)
print(a^b)
print(~a^b)
print(a|~b)
#conditional statements
a=int(input("enter the value"))
if(a>=18):
    print("voter is eligible for voting")
else:
    print("not eligible")
#greatest of three numbers
a=int(input("enter the value1"))
b=int(input("enter the value2"))
c=int(input("enter the value3"))
if(a>b):

    if(a>c):
        print("a is big")
    else:
        print("c is big")
else:
    if(b>c):
        print("b is big")
    else:
        print("c is big")
#looping statements:
for i in range(0,100):
    print(i)
i=0
while(i<20):
    i=i+1
    print(i)

      
