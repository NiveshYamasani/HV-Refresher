class Employee:
    def __init__(self): #constructor
        print('employee created')

    def __del__(self): #destructor
        print('Destructor called Employee deleted')

emp = Employee()
del emp
# emp = Employee()
