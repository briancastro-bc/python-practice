from . import Person

"""
    :excersice 1 and 3
"""
class Employee(Person):
    
    def __init__(self, name: str, salary: float=1000) -> None:
        super().__init__(name)
        self.salary = salary
        
    def set_salary(self, salary: float):
        self.salary = salary
    
    """
        :method pay_duty - Devuelve la información del usuario y especifica si debe pagar o no
        impuesto.
    """
    def pay_duty(self) -> bool:
        if self.salary > 3000:
            print(dict({
                "nombre": self.name,
                "salario": self.salary,
                "mensaje": "Debe pagar impuesto"
            }))
            return True
        print(dict({
            "nombre": self.name,
            "salario": self.salary,
            "mensaje": "No debe pagar impuesto"
        }))
        return False
    