# class Dog:
#     no_of_legs = 4
#     no_of_teeth = 42
#     can_fly = False
#     lay_eggs = False

# class Bird:
#     no_of_legs = 2
#     no_of_teeth = 0
#     have_beak = True

# print(Dog.no_of_legs)

# #Instances or Objects
# golden_retriever = Dog()
# husky = Dog()

# #Left side = name; right side called (constructor: used to initialize variables)
# parrot = Bird()
# eagle = Bird()

# print(husky.no_of_legs)
# print(husky.can_fly)
# print(husky.lay_eggs)
# print(husky.no_of_teeth)


#person class

# class Person:
#     #Double underscore is called dunder
#     #Init = initialized
#     def __init__(self, name, age):
#         #Self = object
#         self.name=name
#         self.age=age
    
#     def display_info(self):
#         print(f"Name: {self.name}, age:{self.age}")

# person1 = Person("joseph", 15)
# print(person1.name)
# print(person1.age)

# person1.display_info()









class Student():
    def __init__(self, name, age, school):
        self.name=name
        self.age=age
        self.school=school
        
    def show_details(self):
        print(self.name)
        print(self.age)
        print(self.school)

joseph = Student()

joseph.show_details("Joseph", 15, "McNeil")
    

















