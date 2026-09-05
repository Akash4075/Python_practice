class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print(f"name of the person is {self.name}, age of the person is {self.age}")

person_info=person("Akash",22)
person_info.display_info()
