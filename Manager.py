print("Manager Loaded")

class Manager:
    jumlah_manager = 0
    list_manager = []

    def __init__(self, ID_number, username, password, Name, Department):
        self.ID_number = ID_number
        self.username = username
        self.password = password
        self.Name = Name
        self.Department = Department
        Manager.jumlah_manager += 1

    def __del__(self):
        Manager.jumlah_manager -= 1

    def getID(self):
        return self.ID_number

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getName(self):
        return self.Name

    def getDepartment(self):
        return self.Department

    def update(self, ID_number, username, password, Name, Department):
        self.ID_Number = ID_number
        self.password = password
        self.Name = Name
        self.Department = Department

def AddManager(idInput, unInput, pwInput, nmInput, dpInput):
    manager1 = Manager(idInput, unInput, pwInput, nmInput, dpInput)
    Manager.list_manager.append(manager1)

def getManagerAllData(pilihan):
    """ Pilihan berisi 1 - 5:
        1. ID number
        2. Username
        3. Password
        4. Name
        5. Department """
    return 
#--------------------------------------------------------------------------

manager1 = Manager(1313618018, "dhimas", "123456", "Dhimas Amri Pratama", "Ilmu Komputer")
Manager.list_manager.append(manager1)
manager1 = Manager(2002, "Adam", "654321", "Adam lOveLace", "Marketing")
Manager.list_manager.append(manager1)

"""for i in range(5):
    a = int(input("ID Number : "))
    b = input("username : ")
    c = input("password : ")
    d = input("name : ")
    e = input("department : ")
    AddManager(a,b,c,d,e)"""
