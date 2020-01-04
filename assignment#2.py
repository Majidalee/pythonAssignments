#TODO takes 5 unser inpputs of different subject marks total it and generate total marks and grades  accorddingly

'''
subject_1=int(input('enter the marks of first subject:: '))
subject_2=int(input('enter the marks of second subject:: '))
subject_3=int(input('enter the marks of third subject:: '))
subject_4=int(input('enter the marks of forth subject:: '))
subject_5=int(input('enter the marks of fifth subject:: '))
total_marks=int(input('enter the total marks::'))

obtained_marks=subject_1+subject_2+subject_3+subject_4+subject_5

average=(obtained_marks/total_marks)*100

if average>=80:
    print('congrats you got A1 Garde')
elif average>=70 and average<80:
    print('congrats you got A Garde')
elif average>=60 and average<70:
    print('congrats you got B Garde')
elif average>=50 and average <60:
    print('congrats you got C Garde')
elif average>=40 and average<50:
    print('congrats you got D Garde')
elif average>=33 and average<=40:
    print('congrats you got F Garde')        
else:
    print('you are Fail: better luck next time')
'''
#TODO even od checking program
'''
number=int(input('enter the number to check even and odd\'ness\n'))
print('odd' if number%2==0 else 'even')
'''

#TODO printing the length of a list
'''
number_list = [12,33,11,33,44]
print(len(number_list))
'''
#sum all numeric items in list
'''
number_list = [12,33,11,33,44]
print(sum(number_list))
'''

#printing numbers that are lesser than 5 in a list
number_list = [1,21,2,3,5,8,13,21,34,55,89]
for i in number_list:
    if i<=5:
        print(i)

