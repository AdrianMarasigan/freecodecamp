class Rectangle:
    def __init__(self, width, height):
        # Constructor initializes a Rectangle instance with specified width and height
        self.width = width
        self.height = height

    def set_width(self, width):
        # Method to set the width of the rectangle
        self.width = width

    def set_height(self, height):
        # Method to set the height of the rectangle
        self.height = height

    def get_width(self):
        # Method to get the width of the rectangle
        return self.width

    def get_height(self):
        # Method to get the height of the rectangle
        return self.height

    def get_area(self):
        # Method to calculate and return the area of the rectangle
        return self.width * self.height

    def get_perimeter(self):
        # Method to calculate and return the perimeter of the rectangle
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        # Method to calculate and return the diagonal length of the rectangle
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        # Method to generate a string representing the rectangle's picture using '*'
        if (self.width > 50):
            return "Too big for picture."

        if (self.height > 50):
            return "Too big for picture."

        line = '*' * self.width  # Number of '*' in each line

        lines = [line for _ in range(self.height)]  # Number of lines in shape

        picture = '\n'.join(lines)

        return picture + "\n"

    def get_amount_inside(self, shape):
        # Method to calculate and return the number of times a given shape can fit inside the rectangle
        w = self.width // shape.width
        h = self.height // shape.height

        return w * h

    def __str__(self):
        # Method to generate a string representation of the rectangle
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"


class Square(Rectangle):
    def __init__(self, side):
        # Constructor initializes a Square instance with a specified side length
        self.width = side
        self.height = side

    def set_side(self, side):
        # Method to set the side length of the square
        self.width = side
        self.height = side

    def __str__(self):
        # Method to generate a string representation of the square
        return "Square(side=" + str(self.width) + ")"
