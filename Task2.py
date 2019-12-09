class AirPlane:


    is_flying = 'false'

    def __init__(self, make, model, years, max_speed, odometr,  km):
           self.make = make
           self.model=model
           self.years=years
           self.max_speed=max_speed
           self.odometr=odometr
           self.km=km

    def take_off(self):
        is_flying=self.is_flying = 'true'
        result = is_flying
        return result

    def land(self):
        is_flying=self.is_flying = 'false'
        result = is_flying
        return result

    def fly(self):
        return (self.odometr - self.km)

    def cons(self):
        return (self.make, self.model, self.years, self.max_speed)


ex1 = AirPlane('AirBus', 'Su-34', '2019', 500, 100, 40)

print(ex1.take_off())
print(ex1.land())
print(ex1.fly())
print(ex1.cons())