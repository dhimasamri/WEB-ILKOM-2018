print("Employee Loaded")

class Employee:
    jumlah_Employee = 0
    list_Employee = []

    def __init__(self, ID_number, Name, Department, SalaryHour, WorkHour, TotalSalary):
        self.ID_number = ID_number
        self.Name = Name
        self.Department = Department
        self.SalaryHour = SalaryHour
        self.WorkHour = WorkHour
        self.TotalSalary = TotalSalary
        Employee.jumlah_Employee += 1

    def __del__(self):
        Employee.jumlah_Employee -= 1

    def getID(self):
        return self.ID_number

    def getName(self):
        return self.Name

    def getDepartment(self):
        return self.Department

    def getSalaryHour(self):
        return self.SalaryHour

    def getWorkHour(self):
        return self.WorkHour

    def getTotalSalary(self):
        return self.TotalSalary

    def update(self, ID_number, Name, Department, SalaryHour, WorkHour, TotalSalary):
        self.ID_Number = ID_number
        self.Name = Name
        self.Department = Department
        self.salaryHour = SalaryHour
        self.WorkHour = WorkHour
        self.TotalSalary = TotalSalary

Employee1 = Employee(100001, "Ada Lovelace", "Marketing", 100000, 0, 0)
Employee.list_Employee.append(Employee1)
Employee1 = Employee(100002, "Hopper", "Marketing", 100000, 0, 0)
Employee.list_Employee.append(Employee1)
Employee1 = Employee(100003, "Roland", "Marketing", 100000, 0, 0)
Employee.list_Employee.append(Employee1)
Employee1 = Employee(100004, "Tilly", "Marketing", 100000, 0, 0)
Employee.list_Employee.append(Employee1)
Employee1 = Employee(100005, "Gracia", "Marketing", 100000, 0, 0)
Employee.list_Employee.append(Employee1)
Employee1 = Employee(100006, "Adam", "Marketing", 100000, 0, 0)
Employee.list_Employee.append(Employee1)
Employee1 = Employee(100007, "Hawa", "Marketing", 100000, 0, 0)
Employee.list_Employee.append(Employee1)
#Employee8 = Employee(000008, "Light", "Marketing", 100000, 0, 0)
