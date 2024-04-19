'''
for i in range(10):
                if i==4:
                        break
                print(i)
print("HHHHHHHHHHHHHHHHHHHHHHHHH")
i=2
while (i<5):
        print(i)
        i=i+1
        
def message():
                print('Helo')
                print('Helo')
                print('Helo')
message()
'''
'''
def add (a,b):
                return a+b
print(add(34,56))


## assert keyword
n =int(input ('enter number'))
assert n>0,"Error"
print("Error")

def adding (a,b):
        return a+b

print (" Sum = ",adding (int(input("enter mumner")), int(input("enter mumner a

gain"))))
'''


'''
n2 = int(input("Enyet a number"))
if n2>0:
        print("Positive")
elif n2<0:
        print("Negeitve")
else:
        print("Zero")

'''
## PYTHON DATA TYPES
        # Fundamental data types

        #-> Numbers (int,float,complex)
        #-> Strings (str)

        # Collection Data types
        #-> Tuple (tuple)
        #-> List  (list)
        #-> Set   (set)
        #->Dictionary (dict)

'''
name ='lawson'
print (len(name))


print("salary {}".format(200))
message = 'python is fun'

# convert message to uppercase
print(message.upper())

# Output: PYTHON IS FUN

# Tuples
# ->created with coma separating values
# ->immutable
'''
"""
lst =[6,8,4,9,0]
lst.insert(3,10)
lst.pop(4)
print(lst)
"""

class Employee:
                eno =101
                name= 'Lawson'
                

                def message(self):
                        print('Message Employee')
#Creating object                      
emp= Employee()
emp.message()
print(emp.eno)
class Employee:
              #Constructor
              #Non-paramiter
              def __init__(self):
                        print('Message Employee Constructor')
              def message(self):
                      print('Message Employee Method')

#Creating object                      
emp= Employee()
emp.message()
print(emp.eno)
