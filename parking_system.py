from slot import ParkingSlot
from vehicle import Vehicle


class ParkingSystem:
    """
        ParkingSystem: An object to store details related to Parking Lot.
        includes 
            parking_slots: parking slot details, 
            next_avail_slot: next available slot (Default -1, to represent no space is available),
            __queue: a queue which provides the minimum slot number in case a vehicle was removed from a slot
    """
    def __init__(self) -> None:
        self.parking_slots: list(ParkingSlot) = []
        self.next_avail_slot = -1
        self.__queue = []

    def create_parking_slots(self, num_of_slots: int) -> str:
        """
            Append empty slots (vehicle data: None) to the parking lot (parking_slots)
            Set next available slot (num_of_slots) to 0 [1st slot in parking_slots] 
        """
        self.parking_slots = []

        for i in range(num_of_slots):
            slot_num = i + 1
            slot = ParkingSlot(slot_num)
            self.parking_slots.append(slot)

        self.set_next_avail_slot()
        return "Create_parking_lot % d" % (len(self.parking_slots))

    def set_next_avail_slot(self, slot_num=None) -> None:
        """
            Set the value for next avail slot (next_avail_slot)
            Handles 4 Case
                1. If vehicle is removed (slot_num), minimum of the current avail slot & the removed slot,
                    is stored as next_avail_slot, the other is added to the queue
                2. In case there are multiple empty slots (in-between the non-empty slots),
                    the min of those slots is chosen from the queue as stored next_avail_slot
                3. If parking lot is full (next_avail_slot = -1)
                4. If the slots are being filled in incremental manner (without any gaps/empty slots),
                    then the next slot is incremented by 1
        """

        if slot_num != None:
            if slot_num < self.next_avail_slot:
                self.__queue.append(self.next_avail_slot)
                self.next_avail_slot = slot_num
            else:
                self.__queue.append(slot_num)

        elif len(self.__queue):
            self.next_avail_slot = min(self.__queue)
            self.__queue.remove(self.next_avail_slot)

        elif self.next_avail_slot == len(self.parking_slots):
            self.next_avail_slot = -1

        else:
            self.next_avail_slot += 1

    def get_next_avail_slot(self) -> int:
        """
            Returns the value of next_avail_slot
            Use: adding next slot in the parking lot
        """
        return self.next_avail_slot

    def assign_vehicle_to_slot(self, registration_number: str,
                               driver_age: int) -> str:
        """
            Checks if next slot is available (avail_slot != -1)
                If yes,
                - stores vehicle's data and assign it to a slot
                - prompts to store the next_avail_slot
        """
        avail_slot = self.get_next_avail_slot()

        if avail_slot != -1:
            vehicle = Vehicle(driver_age, registration_number)
            slot = self.parking_slots[avail_slot]

            slot.add_vehicle_to_slot(vehicle)
            self.parking_slots[avail_slot] = slot

            # set next_avail_slot
            self.set_next_avail_slot()

            return "Car with vehicle registration number \"% s\" has been parked at slot number % d" % (
                registration_number, slot.slot_number)

        else:
            return "No slots are available"

    def remove_vehicle_from_slot(self, slot_num: int) -> str:
        """
            Checks if the slot is valid & slot is empty
                If yes,
                - remove vehicle's data from the given slot
                - prompts to store the next_avail_slot
        """

        if slot_num <= 0 or slot_num > len(self.parking_slots):
            return "Invalid slot number"

        slot_num -= 1
        slot = self.parking_slots[slot_num]

        if not slot.is_slot_available():
            slot_data = slot.get_vehicle_data()
            reg_num = slot_data["registration_number"]
            driver_age = slot_data["driver_age"]

            slot.remove_vehicle_from_slot()
            self.parking_slots[slot_num] = slot

            # reset next_avail_slot
            self.set_next_avail_slot(slot_num)

            return "Slot number % d vacated, the car with vehicle registration number \"% s\" left the space, the driver of the car was of age % d" % (
                slot_num + 1, reg_num, driver_age)

        else:
            return "No vehicle was parked at this slot"

    def get_slot_num_for_driver_of_age(self, driver_age: int) -> str:
        """
            Checks through all the slots, if slot has vehicle parked then,
            - checks for driver's age
        """
        slots = []

        for slot in self.parking_slots:
            if not slot.is_slot_available():
                slot_data = slot.get_vehicle_data()

                if slot_data["driver_age"] == driver_age:
                    slots.append(slot.slot_number)

        return ', '.join(str(slot) for slot in slots)

    def get_slot_num_for_car_with_num(self, registration_number: str) -> int:
        """
            Checks through all the slots, if slot has vehicle parked then,
            - checks for registration_number
        """
        slot_number = 0

        for slot in self.parking_slots:
            if not slot.is_slot_available():
                slot_data = slot.get_vehicle_data()

                if slot_data["registration_number"] == registration_number:
                    slot_number = slot.slot_number
                    break

        return slot_number

    def get_reg_num_for_driver_of_age(self, driver_age: int) -> str:
        """
            Checks through all the slots, if slot has vehicle parked then,
            - checks for driver_age
        """
        reg_nums = []

        for slot in self.parking_slots:
            if not slot.is_slot_available():
                slot_data = slot.get_vehicle_data()

                if slot_data["driver_age"] == driver_age:
                    reg_num = slot_data["registration_number"]
                    reg_nums.append(reg_num)

        return ', '.join(str(reg_num) for reg_num in reg_nums)

    def __repr__(self) -> str:
        return f"Parking Slots: '{self.parking_slots}', " \
               f"Next Available Slot: {self.next_avail_slot}"
