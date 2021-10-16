class Dog:
    breed = 'Alaskan'
    build = 'Medium'

    # my_object.method("foo") which the interpreter translates behind the scenes 
    # into : MyyClass.method(my_object, "foo")
    # This is because most methods do some work with the object they're called on, 
    # so there needs to be some way for that object to be referred to inside the method.
    # By convention, this first argument is called

    def add(self,a,b):
        return a+b
obj1 = Dog()

print("Calling breed using object :",obj1.breed)

print(obj1.build)

print("Calling breed using classname :",Dog.breed)

print("The sum is :", obj1.add(20,30))