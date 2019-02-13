#Pet Class
class Pet:
    
        
    #creates attributes for name,animal type,age, and get_ for all same attributes
    
    def __init__(self, animal_type, age, name):
        
        self.__name = name
        self.__animal_type = animal_type 
        self.__age = age
            
    def set_name(self, name):
            self.__name = name
            
    def set_animal_type(self, animal_type):
            self.__animal_type = animal_type
            
    def set_age(self, age):
            self.__age = age
            
    def get_name(self):
        return self.__name
            
    def get_animal_type(self):
        return self.__animal_type
            
    def get_age(self):
        return self.__age
        
        
#Write a program that creates an object of the class
#and prompts the user to enter name, type and age for
#for his or her pet.


#The data should be stored as the object's attributes.
#Use the objects accessor methods to retrieve the pets name,
#type and age, displaying this data onscreen.


        
