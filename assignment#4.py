# person_details={'first_name':'imran','last_name':'khan','residence':'Pm house','occupation':'Prime_minister'}
# person_details['qualification']='bachelors'
# person_details['qualification']='Masters'
# for key in person_details.keys():
#     print(f'{key}:{person_details[key]}')
# person_details.__delitem__('qualification')




# city={'shenzen':{
#     'population':'12.53M',
#     'country':'China',
#     'known_for':'tech hub of the world/silicon valley'},

#     'bengalore':{
#     'population':'8.462M',
#     'Country':'India',
#     'known_for':'world software hub'},

#     'karachi':{
#     'population':'300M',
#     'Country':'pakistan',
#     'known_for':'among the largest city of the world'},
# }
    
# print(city.items())    


# while(True):
#     age=int(input('enter the age of person'))
#     if age<3:
#         print('its free yay')
#         break
#     elif age>3 and age<=12:
#         print('ticket price is $12')
#         break
#     elif age>12:
#         print('ticket price is $15')
#         break
    

# def favorite_book(title='title'):
#     return f'{title} is one of the favorite book of all time'

# print(favorite_book('rich dad poor dad'))

from random import randint

number=randint(1,30)
print(number)
for chance in range(3):
    guess=int(input('enter a guess: '))
    if guess<number:
        print('ahhh: bring it up')
    elif guess>number:
        print('ah: you are well over it')
    else:
        print('you got It')        