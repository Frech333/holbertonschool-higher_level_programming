#!/usr/bin/python3

class Square:
    """
    This class defines a square.

    A square is a geometric shape with all four sides of equal length and all angles of 90 degrees.
    """

    def __init__(self, side_length):
        """
        Initializes a Square object with a specified side length.

        Args:
            side_length (float): The length of each side of the square.
        """
        self.side_length = side_length

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.side_length ** 2

    def perimeter(self):
        """
        Calculate the perimeter of the square.

        Returns:
            float: The perimeter of the square.
        """
        return 4 * self.side_length
