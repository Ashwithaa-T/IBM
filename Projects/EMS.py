class Employee:
    def _init_(self,name,id,age,salary):
        self.name = name
        self.id = id
        self._age = age
        self._salary = salary

    def get_name(self):
        return self.name
    def get_salary(self):
        return self._salary
    
    def get_age(self):
        return self._age
    
    def set_age(self,age):
        self._age = age
    def set_salary(self,amount):
        self._salary = amount
    def set_id(self,number):
        self.id = number

    def position(self):
        if self._salary>=100000 and self._salary<200000:
            position = "Team leader"
            print(f"Position is {position}")
        elif self._salary>=200000 and self._salary<500000:
            position = "Manager"
            print(f"Position is {position}")
        elif (self._salary>30000 and self._salary < 100000):
            position = "Employee"
            print(f"Position is {position}")
        else:
            print("Not working in this company")
            
    def display(self):
        print(f"Employee name is {self.name}, id is {self.id}, age is {self._age}, and salary is {self._salary}")

    def attendence(self,id):
        if id==self.id:
            print("Employee is Present")
        else:
            print("Employee is Absent")

E1 = Employee("Rajesh",1234988,25,86000)
E2 = Employee("Lalitha",1890675,32,100000)
E3 = Employee("Raghu",3456789,24,60000)
E4 = Employee("Rana",3446789,24,70500)
E5 = Employee("Lalitha",4256789,30,250000)
E1.display()
E1.position()
E2.display()
E2.position()
E3.display()
E3.position()
E4.display()
E4.position()
E5.display()
E5.position()
E1.attendence(1234988)
E2.set_salary(500000)
print(E2.get_salary())
E2.position()
