class ParkingLotLogger:
    def __init__(self):
        self.ticket_log = []

    def log_ticket(self, ticket):
        self.ticket_log.append(ticket)

    def show_log(self):
        for ticket in self.ticket_log:
            print(
                f"Vehicle {ticket.vehicle.vehicle_no} parked at spot {ticket.parking_spot.id} at time {ticket.entry_time}")

