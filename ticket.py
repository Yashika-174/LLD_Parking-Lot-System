import time

class Ticket:
    def __init__(self,entry_time,parking_spot,vehicle):
        self.entry_time=entry_time
        self.parking_spot=parking_spot
        self.vehicle=vehicle

    def calculate_fees(self,exit_time):
        duration = exit_time - self.entry_time
        total_minutes = int(duration / 60)
        per_minute_rate = self.parking_spot.price_per_hour / 60
        return round(per_minute_rate * total_minutes, 2)


