class Family:
    def __init__ (self,surname):
        self.surname=surname
        
class child(Family):
    def __init__ (self,name,surname):
        self.name = name
        super().__init__(surname)
child=child("Akash","Shetty")
print(f"{child.name} {child.surname}")
    