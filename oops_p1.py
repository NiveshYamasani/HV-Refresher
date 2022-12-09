class Car:  #Creating class
    attr1 = 'Audi'
    attr2 = 'BMW'
    attr3 = 'Ferrari'

    def names(self):  #Creating Function
        print("The car name is ",self.attr1)
        print("The car name is ",self.attr2)
        print("The car name is ",self.attr3)

MyCar = Car() #Creating Object - MyCar is object and Car is class
print(MyCar.attr1)
MyCar.names()