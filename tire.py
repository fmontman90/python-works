import math

class Tire:
    """
    Tire reps a tire that would be used with a automobile.
    """

    def __init__(self, tire_type, width, ratio, diameter, brand='', construction='R'):
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.construction = construction

    def circumference(self):
        """
        The circumference of the tire in inches.
        >>> tire =Tire('P', 205, 65, 15)
        >>> tire.circumference()
        80.1
        """
        #side_wall_inches = (self.width * (self.ratio / 100)) /25.4
        total_diameter = self._side_wall_inches() * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    def __repr__(self):
        """
        Rep the tires information in the standard notation present on the side of the tire.
        Example: 'P215/65R15'
        """
        return (f"{self.tire_type}{self.width}/{self.ratio}"
                + f"{self.construction}{self.diameter}")
    
    def _side_wall_inches(self):
        return (self.width * (self.ratio / 100)) /25.4

#Inheriting from TIRE creating subclass 
class SnowTire(Tire):
    def __init__(self, tire_type, width, ratio, diameter, chain_thickness, brand='', construction='R'):
        super().__init__(self, width, ratio, diameter, brand, construction )
        # Tire.__init__(self, width, ratio, diameter, brand, construction ) //This is another way
        # it removes self 
        self.chain_thickness = chain_thickness

    def circumference(self):
        """ The cirum of tire with chain in inches
        >>> tire = SnowTire('P' , 205, 65,15,2)
        >>> tire.circumference()
        92.7
        """
        total_diameter = (self._side_wall_inches() + self.chain_thickness) * 2 + self.diameter
        return round(total_diameter * math.pi, 1)
    
    def __repr__(self):
        return super().__repr__() + "(Snow)"
        





