class person:
    #Attributes
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    #Method
    def display_info(self):
        print(f"name of the person is {self.name}, age of the person is {self.age}")
#Object
person1=person("Akash",21)
person2=person("Chinmayi",21)
person3=person("Rohith",80)

#Calling the Objects
person1.display_info()
person2.display_info()
person3.display_info()