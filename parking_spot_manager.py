from abc import ABC,abstractmethod
from exception import ParkingFullException


class ParkingSpotManager(ABC):
    def __init__(self,spots):
        self.spots=spots

    @abstractmethod
    def findParkingSpace(self):
        pass

    def park_vehicle(self,vehicle):
        spot=self.findParkingSpace()
        if spot.park_vehicle(vehicle):
            return spot

        raise ParkingFullException("No empty parking spot available")

    def remove_vehicle(self,vehicle):
        for spot in self.spots:
            if spot.vehicle and spot.vehicle.vehicle_no==vehicle.vehicle_no:
                spot.remove_vehicle()
                break

    
class TwoWheelerManager(ParkingSpotManager):
    def findParkingSpace(self):
        for spot in self.spots:
            if spot.isEmpty and spot.price_per_hour==10:
                return spot
        return ParkingFullException("No empty two-wheeler spot available")


class ThreeWheelerManager(ParkingSpotManager):
    def find_parking_space(self):
        for spot in self.spots:
            if spot.is_empty and spot.price_per_hour == 15:
                return spot
        raise ParkingFullException("No empty three-wheeler spot available")


class HeavyDutyManager(ParkingSpotManager):
    def find_parking_space(self):
        for spot in self.spots:
            if spot.is_empty and spot.price_per_hour == 30:
                return spot
        raise ParkingFullException(
            "No empty heavy-duty vehicle spot available")
