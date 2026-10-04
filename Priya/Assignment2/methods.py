class Emp:
    companyname = 'IBM'
    def __init__(self,id,name,city):
        self.id = id
        self.name = name
        self.city = city

    def show(self):
        print("Company Name:",Emp.companyname)
        print("ID:",self.id)
        print("Name:",self.name)
        print("City:",self.city)

    @classmethod
    def change_companyname(cls):
        cls.companyname = 'infosys'


Emp.change_companyname()
obj =  Emp(101,'Akash','Pune')
obj.show()


obj1 = Emp(102,'Rahul','Mumbai')
obj1.show()