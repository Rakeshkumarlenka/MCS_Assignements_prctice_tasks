class Employee:
    def __init__(self,a,b,c,d,e):
        self.emp_name = a
        self.emp_id = b
        self.designation = c
        self.net_sal = d
        self.comp_name = e

    def show_emp(self):
        print("employee name =",self.emp_name)
        print("employee id =",self.emp_id)
        print("designation =",self.designation)
        print("net salary =",self.net_sal)
        print("company name =",self.comp_name)

emp=Employee("rakesh",34,"full stack",28000,"MCS")
emp.show_emp()

