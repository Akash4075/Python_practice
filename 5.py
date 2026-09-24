class user:
    def __init__(self,username,passward):
        self.username=username
        self.__passward=passward
        
        
    def get_username(self,username):
        if self.username==username:
            print("login succefully")
        else:
            print("wrong username")
    
    def get_passward(self,passward):
        if self.__passward==passward:
            print("Login Succefully")
        else:
            print("Passward wrong")
    
my_user=user("Akashap",1234)
my_user.get_username("Akasha")
my_user.get_passward(1234)   