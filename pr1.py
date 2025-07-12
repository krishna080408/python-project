print('welcome to introduction')
print("")

name=input("enter your name:")
age=int(input("enter your age:"))
height=(input("enter your height:"))
favourite_number=int(input ("enter your favourite number:"))
print("")
print('thank you for using the personal data collector.goodbye!')
print("")
print("name:",name,"type:",type(name),"memory address;",id(name))
print("age:",age,"type:",type(age),"memory address;",id(age))
print("height:",height,"type:",type(height),"memory address;",id(height))
print("favourite_number:",favourite_number,"type:",type(favourite_number),"memory address;",id(favourite_number))
print("")

import datetime

age=int(input("how old are you?"))
current_year=datetime.datetime.now().year
birth_year=current_year - age
print("you were born in",birth_year)
'''
welcome to introduction

enter your name:krishna
enter your age:17
enter your height:5.1
enter your favourite number:3

thank you for using the personal data collector.goodbye!

name: krishna type: <class 'str'> memory address; 2090727558432
age: 17 type: <class 'int'> memory address; 140722619041192
height: 5.1 type: <class 'str'> memory address; 2090772271088
favourite_number: 3 type: <class 'int'> memory address; 140722619040744

how old are you?17
you were born in 2008
'''
      

      
      
             
