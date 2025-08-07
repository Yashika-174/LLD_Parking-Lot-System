import time


class ExitGate:
    def __init__(self, factory,spots):
        self.factory = factory
        self.spots=spots

    def remove_vehicle(self, ticket):
        manager = self.factory.get_manager(ticket.vehicle.vehicle_type,spots)
        fee = ticket.calculate_fees(time.time())
        print(f"Total fee for vehicle {ticket.vehicle.vehicle_no}: ₹{fee}")
        if manager:
            manager.remove_vehicle(ticket.vehicle)
