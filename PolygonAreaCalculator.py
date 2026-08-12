import math

class Rectangle:
    def __init__(self, width, height) -> None:
        if not (isinstance(height,(int,float)) and isinstance(width,(int,float))):
            raise TypeError ("Invalid height: height should be f type int or float")

        if height < 1 or width < 1:
            raise ValueError ("Invalid height/width: height and width should be greater than 0")

        self.width = width
        self.height = height

    def set_width(self, newwidth: int | float) -> None:
        if not isinstance(newwidth,(int,float)):
            raise TypeError ("Invalid width: width should be f type int or float")

        if newwidth < 1:
            raise ValueError ("Invalid width: width should be greater than 0")


        self.width = newwidth

    def set_height(self, newheight: int | float) -> None:
        if not isinstance(newheight,(int,float)):
            raise TypeError ("Invalid height: height should be f type int or float")

        if newheight < 1:
            raise ValueError ("Invalid height: height should be greater than 0")

        self.height = newheight

    def get_area(self):
        area= self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * (self.width+self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = math.sqrt((self.width**2) + (self.height**2))
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape):
       return (self.width // shape.width) * (self.height // shape.height)

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side) -> None:
        super().__init__(side, side)

    def set_side(self, side: int | float) -> None:
        super().set_width(side)
        super().set_height(side)

    def set_width(self, width: int | float) -> None:
        self.set_side(width)

    def set_height(self, height: int | float) -> None:
        self.set_side(height)

    def __repr__(self):
        return f"Square({self.width}=9)"

# Usage Example

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))