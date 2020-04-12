print("Employee Loaded")

class Employee:
    jumlah_Employee = 0
    list_Employee = []

    def __init__(self, ID_number, Name, Department, SalaryHour, WorkHour, TotalSalary=SalaryHour * WorkHour):
        self.ID_Number = ID_Number
        self.Name = Name
        self.Department = Department
        self.SalaryHour = SalaryHour
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

