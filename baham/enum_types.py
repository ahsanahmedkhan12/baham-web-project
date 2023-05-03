from enum import Enum

class VehicleType(Enum):   
    AUTO_RICKSHAW = "Auto Rickshaw"    
    SEDAN = "Sedan"    
    HATCHBACK = "Hatch Back"    
    SUV = "Sub-Urban Vehicle"    
    VAN = "Van"    
    HIGH_ROOF = "High Roof"    
    MOTORCYCLE = "Moto cycle/Scooter"    
    
    def __str__(self):
        return self.value
