'''
      certified python prgrammer sylani mass training program
                  submitted by Majid Ali
'''

# Question #No1
print("""
twinke twinke little star
      how i wonder what's you are
            up above in the sky
            like a  diamond in the sky
twinke twinke little star
      how i wonder what's you are
""" )

# Question #No2
import sys
print(sys.version)


# Question #No3
from datetime import date
print(date.today())

# Question #No4
first_name=input("enter first name: ")
last_name = input("enter last name: ")
print(f'first name reversed = {first_name[::-1]}\nlast name reversed = {last_name[::-1]}')

# Question #No5

print(int(input("enter first number: "))+int(input('enter second number: ')))

# Question #No6
import math
raduis=int(input("enter radius of circle:"))
print("area={:.2f}".format(math.pi * (raduis ** 2)))
