class ShippingContainer:
    next_serial = 1983 # class attribute is available on both class and instance object 

    # static consts 
    WIDTH = 8.0
    HEIGHT = 8.5

    """ Choose between static method and class method
    1) If need to refer to the class object within the method, e.g. to access class attribute then use class method. Otherwise (no need to access either instance or class attribute) prefer to use staticmethod. 
    
    2)In practice, most static methods are internal implementation details hence prefixing with underscore and since they have no access to class/instance attribute they rarely form a useful part of the class interface. In principle it's possible to implement static methods outside the class at moudle scope with loss of any functionality. So be careful when add a static method as it might be better to factor out into a separate module. @staticmethod decorator merely facilitates a particular logical organisation of code allowing to put within a class what would otherwise be free functions. 

    3) Sometimes it's ideal to have classmethod to support named constructor (also known as factory functions). Multiple named ctors can reduce the complexity of __init__(self) based on different from of instance configuration. 

    """


    """ Static methods and inheritance
    1) static methods can be overridden in python! But to enable this ploymorphism the base class must call the static method using instance identifier 'self' otherwise derived class won't be able to override it if using class instance. 
    
    2) class methods are inherited automatically by the derive class. 
    
    """

    @staticmethod # create a static method
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    @classmethod
    def get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result     
    
    
    # use *args and **kwargs to allow derived class overriding base init 
    @classmethod # using classmethod as a named ctor 
    def create_empty(cls, owner_code, length_ft, *args, **kwargs):
        return cls(owner_code, None, length_ft, *args, **kwargs)
    
    @classmethod
    def create_list(cls, owner_code, items, length_ft, *args, **kwargs):
        return cls(owner_code, list(items), length_ft, *args, **kwargs)

    
  
    def __init__(self, container_code, content, length_ft):
        self.container_code = container_code
        self.content = content
        self.length = length_ft
        # class attribute is best accessed through class name; do NOT use instance object to access it. Assigning to an instance attribute always creates a new attribute on the instance; it never modifies the class attribute.

        # this static method can be overridden as it uses instance object rather than class object to call a static method 
        self.base = self._get_next_serial() 


        # call a class method just like calling a static method 
        self.serial = ShippingContainer.get_next_serial()

    
    @property
    def volume_ft(self):
        return ShippingContainer.WIDTH * ShippingContainer.HEIGHT * self.length


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_DEGREE = 4 # class attribute on a derived class 
    FRIDGE_VOLUME_FT3 = 100 # special case for the derived class 

    # override base init
    def __init__(self, owner_code, content, length_ft, degree):
        # super() is the base class object; call base class init
        super().__init__(owner_code, content, length_ft)

        # set to the property to use the property setter validation!
        self.degree = degree

    
    @property # trun a method into a property attribute 
    def degree(self):
        return self._degree

    @degree.setter # allow a property setter attribute  
    def degree(self, value):
        if value > RefrigeratedShippingContainer.MAX_DEGREE:
            raise ValueError('cannot set higher than max degree')
        self._degree = value


    @property  # override base class property while using the base implemenation.
    def volume_ft(self):
        return super().volume_ft - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3    

    @staticmethod
    def _get_next_serial():
        return 'R000' # overriding the base static method


def test_class_attributes():
    sc1 = ShippingContainer('RES', 'books', 18)
    print(sc1.serial)
    sc2 = ShippingContainer('GDE', 'beef', 18)
    print(sc2.serial)

    empty = ShippingContainer.create_empty("EMP", 18)
    print(empty.container_code)
    list_container = ShippingContainer.create_list("LIS", ("books", "beef", "clothes"), 18)
    print(list_container.content)
    print(list_container.volume_ft)


def test_staticmethod_override():
    r = RefrigeratedShippingContainer("REG", "fish", 20, 2);
    print(r.base)

    # classmethod are inheriated by the derived class 
    emptyRe = RefrigeratedShippingContainer.create_empty("REMP", length_ft = 20, degree = 3)
    print(emptyRe.serial)
    print(emptyRe.degree)
    emptyRe.degree = 3.4
    print(emptyRe.degree)
    listRe = RefrigeratedShippingContainer.create_list("LIRE", ['badminton shoes', 'badminton rackets'], 20, degree = 1)
    print(listRe.content)
    print(listRe.degree)
    print(listRe.base)
    print(listRe.volume_ft)


def main():
    print('test class attributes...')
    test_class_attributes()

   # print('\n')
    print('test static and class method inheritance...')
    test_staticmethod_override()

if __name__ == '__main__':
    main()
