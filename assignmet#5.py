#"Assignment # 4"


#Question # 1

'''
def factorial(num):
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
    return f'the factorial of {num} is {factorial}'
print(factorial(7))        
'''

#Question # 2

# uppper case later and lowerr case later
'''
def string_check(char_string):
    lower_count=0
    upper_count = 0
    for char in char_string:
        if (char.isupper()):
            upper_count +=1
        elif (char.islower()):
            lower_count += 1

    return f'the string {char_string} has upperCase {upper_count} strings and {lower_count} lowerCase strings'  
string_value='tHiS iS mAJiD'              
print(string_check(string_value))            
'''
#Question # 3

'''
list_of_numbers=[1,2,3,4,5,6]
for num in list_of_numbers:
    if num%2==0:
        print(num)
    else:
        pass     
'''

#Question # 4



'''
def reverse(value):
    return value[::-1]
def ispalindrome(value):
    revers=reverse(value)
    if (revers==value):
        return True
    else:
        return False    

print(ispalindrome('bob'))
'''

#Question # 5

'''
def isprime(num):
    for i in (2,num):
        if (num%i!=0):
            print(f'{num} is a prime number')
        else:
            print(f'{num} is not prime number')
            break
            
print(isprime(2))
'''

#Question # 6
'''
def shoping_list(*items):
    return print(*items)
    
    
    # print(items)
shoping_items=input('enter your , seprated shoping items seprated with ').split(',')
items=list(shoping_items)    
print(shoping_list(items))    
'''