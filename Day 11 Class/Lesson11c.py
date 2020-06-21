class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
s= car('remake','Toyota',2014)
print(s.make)
print(s.model)
print(s.year)

print(s.get_descriptive_name())