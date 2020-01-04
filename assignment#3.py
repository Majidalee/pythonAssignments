
# #using oop method for my own practice


# class calculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def addition(self):
#         return self.num1 + self.num2
#     def subtaction(self):
#         return self.num1 - self.num2
#     def multiply(self):
#         return self.num1 * self.num2        
#     def divide(self):
#         return self.num1 / self.num2    
    
# num1=int(input('enter first number: '))
# num2=int(input('enter second number: '))
# calculation=calculator(num1,num2)

# while(True):
#     # print('''
#     # 1:addition
#     # 2:subtract
#     # 3:divide
#     # 4:multiply
#     # 5:exit
#     # ''')
#     operation=int(input('enter value:'))
#     if operation==1:
#         print(calculation.addition())
#         break
#     elif operation==2:
#         print(calculation.subtaction())
#         break
#     elif operation==3:
#         print(calculation.multiply())
#         break
#     elif operation==4:
#         print(calculation.divide())
#         break   
#     elif operation==5:
#         break        
#     else:
#         print('invalid choice')


#check either a list element is numeric or not
'''
my_list=[2,3,9,'majid',16,'hello',11,'world'] 

for i in my_list:
    print(str(i).isdigit())
'''    

#TODO adding a key in dictionary
'''
new_dictory={'name':'majid','fname':'abdulsattar'}
key=input('input the key to retreive a value:: ')
print(new_dictory[key])
'''



#TODO sum all the numbers in a list
'''
my_list=[2,3,9,'majid',16,'hello',11,'world'] 
x=[]
for i in my_list:
    if str(i).isdigit()==True:
        x.append(i)
print(sum(x))        
'''

#TODO identify duplicate elemenets in list

'''
x = [1,1,5,6,2,3,4,2]
duplicates=[num for num in x if x.count(num)>1]
print(duplicates)
'''



#TODO check keys in dictionary
'''
new_dictory={'name':'majid','fname':'abdulsattar'}
searched_key=input('enter the key your are searching for:: ')
if searched_key in new_dictory.keys():
    print('YAY: IT exists')
else:
    print('luckily it Doesn;\'t')    
'''    