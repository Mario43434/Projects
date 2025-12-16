# class students:
#     def __init__(self):
#           self.name = ""
#           self.rno = ""
#     def display(self):
#          print("Name : ",self.name)
#          print("RegNo: " ,self.rno)
# Sam = students()
# Sam.name="Sam"
# Sam.rno="110"
# Sam.display()



# class teacher:
#     def __init__(self,name,regno):
#         self.name = name
#         self.regno = regno
#     def display(self):
#         print("Name : ",self.name  )
#         print("Regno : ",self.regno)

# stu1 = teacher("Rio",12)
# stu2 = teacher("zara",13)
# stu1.display()
# stu2.display()


# class calculator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def add(self):
#         print(self.a+self.b)
#     def sub(self):
#         print(self.a-self.b)
#     def mul(self):
#         print(self.a*self.b)   
#     def div(self):
#         print(self.a/self.b)

# calc = calculator(int(input("enter first number : ")),int(input("enter second number : ")))
# op=str(input("Enter a operator : "))
# if(op == '+'):
#     calc.add()
# elif(op == '-'):
#     calc.sub()
# elif(op == '*'):
#     calc.mul()
# elif(op == '/'):
#     calc.div()
# else:
#     print("invalid operator")


# class lap:
    
#    @classmethod  is used to know there is class method is here in  the lap class

#    @classmethod
#    def charger(cls):
#         cls.charge = "C-type"
#         print("Hello baby")
# lap.charger()



# Multiple inheritence

# class lap():
#     def dad(self):
#         print("dady's lap")
# class mom():
#     def moms(self):
#         print("Mommy")
# class phone(lap,mom):
#     def son(self):
#         print("son's mobile")


# sons = phone()
# sons.dad()
# sons.moms()



# Multilevel inheritence

# class grandpa():
#     def money(self):
#         print("i have money")
# class dad(grandpa):
#      def lap(self):
#          print("dady's lap")
# class son(dad):
#      def phone(self):
#         print("son's mobile")

# sam = son()
# sam.phone()
# sam.lap()
# daddy = dad()
# daddy.money()
# sam.money()


# heirarchy inheritence

# class dad():
#     def money(self):
#         print("my money")
# class son1(dad):
#     pass
# class son2(dad):
#     pass
# class son3(dad):
#     pass


# son = son3()
# son.money() 


# super keyword

class a():
    def __init__(self):
        print("A")
    def display(self):
        print("your in a")
class b():
    def __init__(self):
        super().__init__() #it is used to get the elments from the parents.
        print("B")
    def display(self):
        print("your in b")

class c(b,a):
    def __init__(self):
        super().__init__()
        print("C")
    def display(self):
        print("your in c")

stu1 = c()
