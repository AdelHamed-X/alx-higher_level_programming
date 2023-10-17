#!/usr/bin/python3
"""
The square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representing class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing Square instances"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Size Setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """String Representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args and len(args) != 0:
            counter = 0
            for arg in args:
                if counter == 0:
                    self.id = arg
                elif counter == 1:
                    self.size = arg
                elif counter == 2:
                    self.x = arg
                elif counter == 3:
                    self.y = arg
                counter += 1

        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        Returns dict representation of Rectangle
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
