#loops (printing of number*number from 0 to input)

n = int(input())
i=0
while i<n:
    print(i*i)
    i +=1

# python if-else related ques 
    
n=int(input())
if n % 2==0 and n>=2 and n<=5:
    print("Not Weird")
elif n %2==0 and n>=6 and n<=20:
    print("Weird")
elif n %2==0 and n>20:
    print("Not Weird")
else:
    print("Weird")
    
# division question
    
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# writing the function and use of conditionals 
    
def is_leap(year):
    leap = False
    
    if year %100!=0 and year %4==0:
        leap = True
    elif year %400==0:
        leap=True

    return leap
    
year = int(input())
print(is_leap(year))


# used typecasting and printed the desired output 

n = int(input())
s = ''
for i in range(1, n+1):
    print(str(i), end='')


