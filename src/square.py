
"""
    :exercise 2
"""
class Square:
    
    def __init__(self, side: float) -> None:
        self.side = side
    
    def calculate_perimeter(self) -> float:
        perimeter: float = self.side*4
        return perimeter
    
    def calculate_area(self) -> float:
        area: float = self.side*self.side
        return area