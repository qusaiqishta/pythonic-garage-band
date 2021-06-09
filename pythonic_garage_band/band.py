from abc import ABC ,abstractmethod

class Band:
    bands=[]

    def __init__(self,name,members):
        self.name=name
        self.members=members
        Band.bands.append(self)
        print(Band.bands)


    def play_solos(self):
        solos=[]
        
        for member in self.members:
            check_instrument=str(member)

            if check_instrument=='guitar':
                solos.append('face melting guitar solo')
            elif check_instrument=='bass': 
                solos.append('bom bom buh bom')
            elif check_instrument=='drums':
                solos.append('rattle boom cras')
        return solos


    @classmethod
    def __repr__(self):
        print(f"{self.name} is the Band name") 

    def __str__(self):
        print(f"{self.name} is the Band name")

    def to_list(cls):
        return cls.bands  # which will count all bands 


class Musician:
    musicians=[]

    def __init__(self,name,instrument,play_soloo,fame_year):
        self.name = name
        self.instrument=instrument
        self.play_soloo=play_soloo
        self.fame_year=fame_year

        Musician.musicians.append(name)

    def __str__(self):
        return(f' {self.name} usually play {self.instrument} ') 

    def __repr__(self):
        return(f'{self.name} get famus at {self.fame_year}')  


    def get_instrument(self):
        return(self.instrument)

    def play_solo(self):
        return (self.play_soloo)


class Guitarist(Musician):
    play_soloo='face melting guitar solo'
    instrument='guitar'
    fame_year=1997
    def __init__(self, name ):
        super().__init__(name,Guitarist.instrument, Guitarist.play_soloo, Guitarist.fame_year)


class Drummer(Musician):
    instrument='drums'
    play_soloo='rattle boom cras'
    fame_year=1981
    def __init__(self, name):
        super().__init__(name, Drummer.instrument, Drummer.play_soloo, Drummer.fame_year)   


class Bassist(Musician):
    instrument='bass'  
    fame_year=1897
    play_soloo='bom bom buh bom'
    def __init__(self, name):

        super().__init__(name, Bassist.instrument, Bassist.play_soloo,Bassist.fame_year)             




        