class Person:
    def __init__(self, firstname, lastname, birthdate, isFemale):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.isFemale = isFemale


class Employee(Person):
    def __init__(self, firstname, lastname, birthdate, isFemale):
        super().__init__(firstname, lastname, birthdate, isFemale)

class DepartmentHead(Employee):
    def __init__(self, firstname, lastname, birthdate, isFemale):
        super().__init__(firstname, lastname, birthdate, isFemale)


class Department:
    employees = []

    def __init__(self, nameDepartment):
        self.nameDepartment = nameDepartment

    def addEmployee(self, employee):
        for i in self.employees:
            if isinstance(i, DepartmentHead):
                return "Es gibt bereits einen DepartmentHead"
            else:
                self.employees.append(employee)

    def countEmployees(self):
        return len(self.employees)


class Company(Department):
    departments = []

    def __init__(self, nameCompany):
        self.nameCompany = nameCompany

    def addDepartment(self, department):
        self.departments.append(department)

    def countDepartments(self):
        return len(self.departments)

    def countEmployee(self):
        numberEmployees = 0
        for i in self.departments:
            numberEmployees = super().countEmployees()
        return numberEmployees

    def getBiggestDepartment(self):
        depSize = 0
        for i in self.departments:
            if len(i) > depSize:
                depSize = len(i)
                biggestDepartment = i
            else:
                continue
        return biggestDepartment

    def getMaleFemaleRatio(self):
        counterMale = 0
        for department in self.departments:
            for employee in department:
                if employee.isFemale == False:
                    counterMale += 1
                else:
                    continue
        maleRatio = (counterMale / self.countEmployee()) * 100
        femaleRatio = 100 - maleRatio
        return str(maleRatio) + "% of the employees are male and " + str(femaleRatio) + "% of the employees are female"

def main():
    company = Company("Firma123")
    dep1 = Department("MB")
    dep2 = Department("WI")
    dep3 = Department("ET")
    emp1 = Employee("Jonas", "Kirchmair", "06.05.2005", False)
    emp2 = Employee("Julia", "Biechl", "01.09.2005", True)
    emp3 = Employee("Patrick", "Klaric", "29.11.2004", False)
    dph = DepartmentHead("Oliver", "Brandstetter", "25.06.2005", False)
    dph2 = DepartmentHead("Eva", "Bobchev", "25.06.2005", False)

    company.addDepartment(dep1)
    company.addDepartment(dep2)
    company.addDepartment(dep3)

    dep1.addEmployee(emp1)
    dep1.addEmployee(dph)
    dep1.addEmployee(dph2)
    dep2.addEmployee(emp2)
    dep3.addEmployee(emp3)

    print(isinstance(emp1, Employee))
    print(isinstance(emp1, Person))
    print(isinstance(emp1, Department))

    print(dep1.employees)

    print(dep1.countEmployees())
    print(dep2.countEmployees())
    print(dep3.countEmployees())


if __name__ == "__main__":
    main()


