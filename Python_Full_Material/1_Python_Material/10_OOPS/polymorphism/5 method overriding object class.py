while developing web applications, most of the classes are pre-defined classes,
so we define a user-defined class which extends pre-defined class and overrides the methods
of that pre-defined class


class object:
    def __hash__(self):
        ............#generates hashcode(address)
        ............#here it has code to print hash code value(addres)
        ............

class int(object):
    def __hash__(self):
        ............
        ............#here it wont print hashcode value, bcoz here
        ............it is overriden with diferent code
                     here the method has code to print the content
                     but not hash code(address)
    
