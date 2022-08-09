from vehicle import Vehicle


class ParkingSlot:
    """
        Slot: An object to store details related to slot.
        includes 
            slot number (slot_number), 
            vehicle details (vehicle),
            if the slot is available for parking (is_available)
    """
    def __init__(self, slot_num: int) -> None:
        self.slot_number = slot_num
        self.vehicle = None
        self.is_available = True

    def is_slot_available(self) -> bool:
        """
            Returns if the slot is available
            Use: While adding/removing/fetching data of a vehicle
        """
        return self.is_available

    def get_vehicle_data(self) -> dict:
        """
            Returns the details of the vehicle
            Use: fetching all / particular values from vehicle's data
        """
        return {
            "driver_age": self.vehicle.driver_age,
            "registration_number": self.vehicle.registration_number
        }

    def add_vehicle_to_slot(self, vehicle: Vehicle) -> None:
        """
            Add a vehicle to the slot
            & the availability for parking false
        """
        self.vehicle = vehicle
        self.is_available = False

    def remove_vehicle_from_slot(self) -> None:
        """
            Remove the vehicle from the slot
            & make the availability for parking true
        """
        self.vehicle = None
        self.is_available = True

    def __repr__(self):
        return f"Slot Number = {self.slot_number}, \n" \
               f"Vehicle = [{self.vehicle}], \n" \
               f"Is slot available = '{self.is_available}'"
