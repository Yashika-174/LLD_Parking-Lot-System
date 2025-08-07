class ParkingSpot:
    def __init__(self,spot_id,price_per_hour,floor):
        self.spot_id=spot_id
        self.price_per_hour=price_per_hour
        self.floor=floor
        self.vehicle=None
        self.isEmpty=True

    
    def park_vehicle(self,vehicle):
        self.vehicle=vehicle
        self.isEmpty=False
    
    def remove_vehicle(self):
        self.vehicle=None
        self.isEmpty=True





