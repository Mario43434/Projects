# def add(a,b,c=0):
#     print(a+b+c)
# add(1,2)
# add(1,2,3)

    
# class animal():
#     def sound1(self):
#         print("Animal make a sound")
# class dog(animal):
#     def sound(self):
#         print("dog barks")
# class birds(animal):
#     def sound(self):
#         print("bird sings")

# b1 = birds()
# b1.sound()


# class shape():
#     def area(self):
#         return 0
# class rectangle(shape):
#     def area(self):
#         l = 10
#         b = 10
#         return l*b
    
# shape1 = rectangle()
# print(shape1.area())



class person():
    def __init__(self,name):
        self.name = name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
    def display(self):
        print(self.name)
        print(self.grade)

s1 = student("Ram","A")
s1.display()


        
# class vehicle():
#     def start(self):
#         print("vehicle started")
# class car(vehicle):
#     def start(self):
#         print("car started")
    
# car1 = car()
# car1.start()


# class employee():
#     def __init__(self,name,salery):
#         self.name= name
#         self.salery=salery
# class manager(employee):
#     def __init__(self, name, salery,department):
#         super().__init__(name, salery)
#         self.depart = department
#     def display(self):
#         print(self.name)
#         print(self.salery)
#         print(self.depart)

# emp1 = manager("RAM","10000","IT")
# emp1.display()