from parking_spot_manager import (
    TwoWheelerManager, FourWheelerManager, ThreeWheelerManager, HeavyDutyManager)

from vehicle_type import VehicleType


class ParkingSpotManagerFactory:
    def get_manager(self, vehicle_type, spots):
        if vehicle_type ==  VehicleType.TWOWHEELER:
            return TwoWheelerManager(spots)
        elif vehicle_type == VehicleType.FOURWHEELER:
            return FourWheelerManager(spots)
        elif vehicle_type == VehicleType.THREEWHEELER:
            return ThreeWheelerManager(spots)
        elif vehicle_type == VehicleType.HEAVYDUTY:
            return HeavyDutyManager(spots)
        raise ValueError(f"Invalid vehicle type: {vehicle_type}")
