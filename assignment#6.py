# Question#1

'''
An object is a real world entity, everything  in this world is an object having its own functionalities behaviours and methods The key notion is that of an object. An object consists of two things:
data and functions (called methods) that work with that data. As an example, strings in Python are objects. The data of the string object is the actual characters that make up that string. The methods are things like lower, replace, and split. In Python, everything is an object. That includes not
only strings and lists, but also integers, floats, and even functions themselves.

EG: consider a human as a object actually it is..

a human has attrubutes like : Height ,weight etc
a human aslo has methods which he perfom: walking running eating etc
'''

# Question  # 2
'''
As compared to procedural programinng languages object oriented programing is better in minimizaing the compelexity and data redundency,code written in OOP methodology provides better code redablility and optimisation .In object-oriented programming there is a concept called inheritance where you can create a class
that builds off of another class. When you do this, the new class gets all of the variables and methods of the class it is inheriting from (called the base class), this results in code clerance and code minimization at same time.
'''



#Question#3
'''
3.1 function 
A function is a snippet of a code having its  own scope in which we pass a argument to it and it exxecutes the snippet and perform some mathematical and logical opereation on a given argument and at the end it reuturn the result of that operation
eg:a function to determine weather a numbeer is even or add
 
 
3.2  Method

on the other hand  a method is a specific function which defines some characters of an objects in programing world a class, a method will be executed when we call it now when the instace is used,a method can be called any numeber of times with different data,just like fuction bussiness logic is written in the method

Eg: human.walk() here's a method named walk is called whiich is related to human object.
'''

# Question#4
'''
Object: an object is a real world entity having existance in real world 
class: to mdoel a real world object we need a some sort of bluePrint to mock its functionality so a class is a blue print of a real world obejct
attribute: an object has its set of attributes which differenciate it from rest of objects such as its dynamics,hight,weight,color,size
behavior:every object has its own set of behaaviours methods which it perfoms in realworld such as walk,run,eat 
'''

# Question#5
'''
class car:
    def __init__(self,company,name,model,reg_no,power):
        self.company=company
        self.name=name
        self.model=model
        self.reg_no=reg_no
        self.power=power
    def details(self):
        return f'this is a {self.name} car  of {self.model} model'
    def status(self):
        return f'and now the {self.model} is full in the trend'
    def run(self):    
        return f'and now the {self.company}\'s car is running at full {self.power}CC'
    
def main():
    car1=car('toyota','carolla','XLI-2009','awa-200','1200cc')
    car2=car('Suzuki','vagnor','vxr-2019','agx-380','900cc')
    car3=car('audi','v8','2018','am-3212','1600cc')
    car4=car('lamborghini','avendator','2006','kng-516','1800cc')
    car5=car('porche','carena GT','2010','tos-786','1800cc')
    print(car5.run())
main()
'''



















