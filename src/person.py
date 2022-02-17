from abc import ABC
from typing import Any

"""
    :excersice 4 and 5
"""
class Person(ABC):
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    def __init__(self, name: str, age: int=None) -> None:
        self._name = name
        self._age = age
    
    """
        :method __call__ - Es invocado cuando se llama a la instancia de la clase.
    """
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        # __call__ can be use when the __init__ methods doesn't return any value or its value is None.
        return "Person class was called"

    def set_info(self, age: int):
        if not self._age:
            self._age = age
    
    def get_info(self):
        return dict({
            "Nombre": self._name,
            "Edad": self._age
        })