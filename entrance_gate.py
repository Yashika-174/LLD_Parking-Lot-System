import time
from ticket import Ticket


class EntranceGate:
    def __init__(self, factory, logger):
        self.factory = factory
        self.logger = logger

    def find_factory_space(self, vehicle_type, spots):

        manager = self.factory.get_manager(vehicle_type, spots)
        return manager.find_parking_space()

    def generate_ticket(self, vehicle, spot):
        spot.park_vehicle(vehicle)
        ticket = Ticket(time.time(), spot, vehicle)
        self.logger.log_ticket(ticket)
        return ticket
