class company():
   
    def __init__(self):
        self.__company = "Google" # using self.__   this is default it cannot be changed cause it is private variable
    def display(self):
        print(self.__company)

co = company()
co.display()


      
    