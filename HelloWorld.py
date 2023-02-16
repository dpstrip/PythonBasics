class Person:
     def __init__(self, name, age):
        self.name = name  
        self.age = age
     def getName(self):
        print("Your name is " + self.name)
     def getAge(self):
        print("Your age is " + self.age)
    
#this is a fucntion  
 #Must be at the bgginning of file
def HelloWorld():
    print("HelloWorld")
    
print("Hello World")

num1 = 2

if(num1 > 3):
    print("True")
else:
    print("false")
 # This is a multi line comment

list1 = ["Apples", "Banana", "Cheeries"]
tup1 = {13, 12, 15}

for item in list1:
    print(item)
    
for item in tup1:
    print(item)
    
for i in range(1,13):
    print(i)
    
for i in range(0,13,2):
    print(i)

for i in range(0,51,5):
    print(i)
    HelloWorld()
    
HelloWorld()


p1 = Person("Bob", "22")    
p1.getName()
p1.getAge()
    
    
    
    