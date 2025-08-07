🅿️ Parking Lot System in Python

A modular, object-oriented Parking Lot Management System built in Python. Designed with a clean architecture using core OOP principles, this system supports:

Multiple vehicle types: Two-Wheeler, Three-Wheeler, Four-Wheeler, Heavy-Duty

Dynamic pricing based on time (per-minute rate)

Entry and Exit flow with tickets and fee calculation

Strategy + Factory Pattern for extensibility

🚗 Vehicle Support

Vehicle Type

Price/Hour

Manager Class

TwoWheeler

₹10/hr

TwoWheelerManager

ThreeWheeler

₹15/hr

ThreeWheelerManager

FourWheeler

₹20/hr

FourWheelerManager

HeavyDuty

₹30/hr

HeavyDutyManager

📁 Project Structure

parking_lot/
├── vehicle_type.py          # Enum-like constants for vehicle types
├── vehicle.py               # Vehicle class
├── parking_spot.py          # Parking spot with availability tracking
├── exception.py             # Custom exception class
├── parking_spot_manager.py  # Abstract + concrete managers
├── factory.py               # ParkingSpotManagerFactory
├── ticket.py                # Ticket with entry time and fee logic
├── logger.py                # Logs tickets
├── entrance_gate.py         # Entry gate logic
├── exit_gate.py             # Exit gate logic
├── main.py                  # System orchestration

🔁 Core Workflow

main.py

Initializes 100 parking spots across 4 vehicle types

Creates a Vehicle

Handles entry using EntranceGate

Handles exit using ExitGate

Calculates time-based fee and prints it

Ticket System

Entry timestamp recorded

On exit, minutes are calculated

Fee is calculated using: price_per_hour / 60 * total_minutes

Logging

Each ticket is logged using ParkingLotLogger

🧠 Design Patterns Used

Factory Pattern: ParkingSpotManagerFactory returns appropriate manager.

Strategy Pattern: Each vehicle type has its own Manager.

Abstraction via ABC: ParkingSpotManager is an abstract base class.

🧪 Example Execution

$ python main.py
Vehicle 123 parked at Spot 99 on Floor 4
Total fee for vehicle 123: ₹30.0
Vehicle 123 parked at spot 99 at time 1699900000.00

🧩 Future Enhancements

Web API (FastAPI/Flask)

Reservation system

Payment integration

Floor-wise dashboard

GUI frontend (Tkinter or Web)

🛠 Requirements

Python 3.7+

No external libraries required

📄 License

This project is open-sourced for educational and non-commercial use.

🙋‍♀️ Author

Made with ❤️, patience, and plenty of caffeine by Yashika

If you liked this project, don’t forget to ⭐ the repo and share love 💌

For a detailed system diagram, refer to the provided PNG in /docs/diagram.png

