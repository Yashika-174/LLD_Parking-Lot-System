from vehicle_type import VehicleType
from vehicle import Vehicle
from parking_spot import ParkingSpot
from factory import ParkingSpotManagerFactory
from entrance_gate import EntranceGate
from exit_gate import ExitGate
from logger import ParkingLotLogger



if __name__ == "__main__":
    spots = []
    for i in range(1, 101):
        if i <= 25:
            price = 10
        elif i <= 50:
            price = 15
        elif i <= 75:
            price = 20
        else:
            price = 30
        floor = (i - 1) // 25 + 1
        spots.append(ParkingSpot(i, price, floor))

    factory = ParkingSpotManagerFactory()
    logger = ParkingLotLogger()
    entrance = EntranceGate(factory, logger)
    exit_gate = ExitGate(factory,spots)

    vehicle = Vehicle(123, VehicleType.HEAVYDUTY)
    
    try:
        spot = entrance.find_parking_space(vehicle.vehicle_type, spots)
        ticket = entrance.generate_ticket(vehicle, spot)
        print(f"Vehicle {vehicle.vehicle_no} parked at Spot {spot.id} on Floor {spot.floor}")

        exit_gate.remove_vehicle(ticket)
        logger.show_log()
        
    except Exception as e:
        print(str(e))
