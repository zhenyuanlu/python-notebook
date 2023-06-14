import math

class Circle:
    def __init__(self, radius, unit='cm'):
        self.unit = unit
        self.radius = radius  # Radius in specified unit

    @property
    def area(self):
        return math.pi * self._radius**2

    @property
    def circumference(self):
        return 2 * math.pi * self._radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if self.unit == 'inch':
            self._radius = radius * 2.54  # Convert from inch to cm
        else:
            self._radius = radius

    @property
    def radius_inch(self):
        return self._radius / 2.54  # Convert from cm to inch

circle_1 = Circle(3)  # Radius in cm
print(circle_1.radius)  # Output: 3
print(circle_1.radius_inch)  # Output: 1.1811 (3 cm in inches)

circle_2 = Circle(4, 'inch')  # Radius in inches
print(circle_2.radius)  # Output: 10.16 (4 inches in cm)
print(circle_2.radius_inch)  # Output: 4
