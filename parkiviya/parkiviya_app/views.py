class ParkingSpot:
    def __init__(self, level, spot_number):
        self.level = level
        self.spot_number = spot_number
        self.vehicle_number = None

    def is_empty(self):
        return self.vehicle_number is None

class ParkingLot:
    def __init__(self):
        self.spots = {}  # Store parking spots
        self.create_parking_spots()

    def create_parking_spots(self):
        for level in ['A', 'B']:
            start = 1 if level == 'A' else 21
            end = 21 if level == 'A' else 41
            for spot_number in range(start, end):
                key = f"{level}-{spot_number}"
                self.spots[key] = ParkingSpot(level, spot_number)

    def assign_parking_spot(self, vehicle_number):
        for spot_key, spot in self.spots.items():
            if spot.is_empty():
                spot.vehicle_number = vehicle_number
                return {"level": spot.level, "spot": spot.spot_number}
        return None

    def retrieve_parking_spot(self, vehicle_number):
        for spot in self.spots.values():
            if spot.vehicle_number == vehicle_number:
                return {"level": spot.level, "spot": spot.spot_number}
        return None

def main():
    parking_lot = ParkingLot()
    while True:
        print("Parking Lot Management System")
        print("1. Assign Parking Spot")
        print("2. Retrieve Parking Spot")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            vehicle_number = input("Enter the vehicle number: ")
            spot_info = parking_lot.assign_parking_spot(vehicle_number)
            if spot_info:
                print(f"Parking spot assigned: {spot_info}")
            else:
                print("Parking lot is full.")

        elif choice == "2":
            vehicle_number = input("Enter the vehicle number: ")
            spot_info = parking_lot.retrieve_parking_spot(vehicle_number)
            if spot_info:
                print(f"Vehicle is parked at: {spot_info}")
            else:
                print("Vehicle not found in the parking lot.")

        elif choice == "3":
            break

if __name__ == "__main__":
    main()

