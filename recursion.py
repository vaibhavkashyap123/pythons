#max_arr
def max_arr(arr,n):
    if n==1:
        return arr[0]
    return max(arr[n-1],max_arr(arr,n-1))
arr=[14,66,32,55]
n=max_arr(arr,4)
print(n)
def f(n):
    if n<=1:
        return 1
    else:
        return f(n-1)+f(n-2)+f(n-3)
n=f(5)
print(n)
def fibb(n):
    if n in [0,1]:
        return n
    else:
        return fibb(n-1)+fibb(n-2)
fibbonaci=fibb(6)
print(fibbonaci)
#palindrome
def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a=str(input("Enter string:"))
if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")
    #power things
'''

def power(base,exponent):
    if(exponent==0):
        return 1
    else:
        return base*power(base,exponent-1)
base=int(input("enter the base: "))
exponent=int(input("enter the power: "))
n=power(base,exponent)
print("the power {} and the base {} so the answer  {}".format(exponent,base,n))
'''
'''
def factorial(num):
    if(num==0):
        return 1
    else:
        return num*factorial(num-1)
n=factorial(5)
print(n)
'''
def array_mul(arr,n):
    if n<len(arr):
        return 0
    else:
        return n*(arr,n+1)
import array
arr=array.array('i',[1,2,3,4])
sum=array_mul(arr,0)
def array_sum(arr):
    if len(arr)==0:
        return 0
    else:
        return arr[0]+array_sum(arr[1:])
sum=array_sum([1,2,3,4,5,6,7])
print(sum)
def array_div(arr):
    if len(arr)==0:
        return 0
    else:
        return arr[0]**5+array_div(arr[1:])
expo=array_div([1,2,5,6,7])
print(expo)
def recursive(num):
    if num==0:
        return 0
    else:
        return num+recursive(num-1)
sum=recursive(6)
print(sum)
