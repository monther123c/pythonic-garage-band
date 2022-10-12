class Musician() :

    def __init__(self,name):
        print('constractor of parent')
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"
    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"   


    def get_instrument(self):
        print('print from parent')
    def play_solos(self):
        pass  
    def play_solo(self):
        return self.play_solos()

class Band() :

    instances = []     
    def __init__(self,name,members):
        self.name = name
        self.members = members
        Band.instances.append(self)
    
    def play_solos(self):
        solos = []
        for obj in self.members:
            solos.append(obj.play_solos())

        return solos

    @classmethod
    def to_list(cls):
        return cls.instances
    
class Guitarist(Musician) :
    
    def __init__(self,name):
        self.name = name

    def get_instrument(self):
        return 'guitar'

    def play_solos(self):
        return 'face melting guitar solo'

class Bassist(Musician) :

    def __init__(self,name):
        self.name = name

    def get_instrument(self):
        return 'bass'

    def play_solos(self):
        return 'bom bom buh bom'

class Drummer(Musician) :

    def __init__(self,name):
        self.name = name

    def get_instrument(self):
        return 'drums'

    def play_solos(self):
        return 'rattle boom crash'