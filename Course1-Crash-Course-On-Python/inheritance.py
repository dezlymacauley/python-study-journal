class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

# NOTE: Inheritance

# In this example the Apple and Grape class,
# will inherit the functionality of the grape class

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass
