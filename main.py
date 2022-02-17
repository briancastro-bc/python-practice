#!/usr/bin/env python3

from src import Person, Employee, Square

def main():
    employee = Employee("Lola", 2000)
    employee.pay_duty()
    square = Square(6)
    print(square.calculate_perimeter())
    print(square.calculate_area())

if __name__ == '__main__':
    main()