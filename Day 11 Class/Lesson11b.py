class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting")
    def roll_over(self):
        """Simulating rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

k = Dog('Tom',5)


print(k.name)
print(k.age)

k.sit()
k.roll_over()
print(k.roll_over.__doc__)