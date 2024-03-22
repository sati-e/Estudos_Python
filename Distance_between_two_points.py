import math

# mathematical expression
def calculation(point1, point2):
    distance = math.sqrt(pow((point1.get_x() - point2.get_x()), 2) + pow((point1.get_y() - point2.get_y()), 2))
    return distance


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def get_x(self):
        return self.x

    # set new value for x
    def set_new_x(self, new_x):
        self.x = new_x
        if isinstance(new_x, (int, float)):
            self.x = new_x
        else:
            print("Invalid input")

    def get_y(self):
        return self.y

    # set new value for y
    def set_new_y(self, new_y):
        self.y = new_y
        if isinstance(new_y, (int, float)):
            self.y = new_y
        else:
            print("Invalid input")
    # print on screen
    def __str__(self):
        dados = f"({self.x}, {self.y})"
        return dados


if __name__ == '__main__':
    # creating objects and testing
    p1 = Point(2, 3)
    p2 = Point(3, 0)
    print(f"Point 1: {p1} \nPoint 2: {p2}")
    print("Distance between points: ", int(calculation(p1, p2)))
    p2.set_new_x(1)
    p2.set_new_y(1)
    print(f"Point 1: {p1} \nPoint 2: {p2}")
    print("Distance between points: ", int(calculation(p1, p2)))