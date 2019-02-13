import pet

def main():

    name = input("Enter your pet's name: ")
    
    print(name)

    animal_type = input('Enter animal type: ')
    
    print(animal_type)

    age = float(input('Enter the age of your animal: '))
    
    print(age)

    #creating an object of pet clas
    my_Pet = pet.Pet(animal_type, age, name)

    print("Your pet's name is: ",my_Pet.get_name())
    
    print("The type of animal you have is: ",my_Pet.get_animal_type())
    
    print("Your pet's age:  ",my_Pet.get_age())
    
main()
