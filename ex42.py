# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

#


class Dog(Animal):
    # Create a class named Dog that is-a Animal

    def __init__(self, name):
        # From self get attribute name and set it to name
        self.sit = False
        self.name = name
        print "%s have no ticks" % self.name
        print


class Cat(Animal):
    # Create a class named Cat that is-a Animal

    def __init__(self, name):
        ##
        self.name = name


class Person(object):

    def __init__(self, name):
        ##
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

#


class Employee(Person):

    def __init__(self, name, salary):
        ##
        super(Employee, self).__init__(name)
        ##
        self.salary = salary

        print "%s's salary is $%d" % (self.name, self.salary)


class Fish(object):
    # Create a class named Fish that is-a object
    pass


class Salmon(Fish):
    # Create a class named Salmon that is-a Fish
    pass


class Halibut(Fish):
    # Create a class named Halibut that is-a Fish
    pass

# rover is-a Dog
rover = Dog("Rover")

# Satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# From mary get the pet attribute and set it to satan
mary.pet = satan

# Set frank to an instance of class Employee that takes "Frank" and 120000
# parameters
frank = Employee("Frank", 120000)

# From frank get the pet attribute and set it to rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
