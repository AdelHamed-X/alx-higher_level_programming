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
