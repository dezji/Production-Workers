# Author Name: Deziallia Morris

class Employee:

    def __init__(self, employeeName, employeeNumber):
        self.__employeeName = employeeName
        self.__employeeNumber = employeeNumber

    def set_employeeName(self, employeeName):
        self.__employeeName = employeeName

    def set_employeeNumber(self, employeeNumber):
        self.__employeeNumber = employeeNumber

    def get_employeeName(self):
        return self.__employeeName

    def get_employeeNumber(self):
        return self.__employeeNumber


class ProductionWorker(Employee):

    def __init__(self, employeeName, employeeNumber, shiftNumber, hourlyPayRate):
        Employee.__init__(self, employeeName, employeeNumber)
        self.__shiftNumber = shiftNumber
        self.__hourlyPayRate = hourlyPayRate

    def set_shiftNumber(self, shiftNumber):
        self.__shiftNumber = shiftNumber

    def set_hourlyPayRate(self, hourlyPayRate):
        self.__hourlyPayRate = hourlyPayRate

    def get_shiftNumber(self):
        if self.__shiftNumber == 1:
            return "Day"
        if self.__shiftNumber == 2:
            return "Night"

    def get_hourlyPayRate(self):
        return self.__hourlyPayRate


def main():

    employeeName = input("Please enter employee name: ")
    employeeNumber = input("Please enter employee number: ")
    shiftNumber = int(input("Please enter shift number (1 for day, 2 for night): "))
    hourlyPayRate = float(input("Please enter hourly pay rate: "))

    employee = ProductionWorker(employeeName, employeeNumber, shiftNumber, hourlyPayRate)

    print("Employee information entered.\nHere are the results:\n")
    print("Employee name:", employee.get_employeeName())
    print("Employee number:", employee.get_employeeNumber())
    print("Employee shift:", employee.get_shiftNumber())
    print("Employee hourly pay rate:", format(employee.get_hourlyPayRate(), ",.2f"))


main()
