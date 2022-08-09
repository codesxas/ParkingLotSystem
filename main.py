from parking_system import ParkingSystem


class ReadInputFile:
    """
        Input: takes input file path
        Output:
          1. Creates a parking-lot system
          2. parse the input files and executes commands based upon each line
    """
    def __init__(self, file_path):
        self.parking_system = ParkingSystem()
        self.parse_input_file(file_path)

    def parse_input_file(self, file_path):
        file = open(file_path, 'r')
        input_data = file.readlines()

        for _line in input_data:
            __input = _line.strip().split()
            self.assign_input_functions(__input)

    def assign_input_functions(self, __input: list):
        switcher = {
            "Create_parking_lot": self.create_parking_lot,
            "Park": self.park,
            "Leave": self.leave,
            "Slot_numbers_for_driver_of_age": self.slot_numbers_for_driver_of_age,
            "Slot_number_for_car_with_number": self.slot_number_for_car_with_number,
            "Vehicle_registration_number_for_driver_of_age": self.vehicle_registration_number_for_driver_of_age
        }

        switcher.get(__input[0], 'Invalid Input!!')(__input)

    def create_parking_lot(self, __input: list) -> None:
        num_of_slots = int(__input[1])

        res = self.parking_system.create_parking_slots(num_of_slots)
        print(res)

    def park(self,  __input: list) -> None:
        reg_num = __input[1]
        driver_age = int(__input[3])

        res = self.parking_system.assign_vehicle_to_slot(reg_num, driver_age)
        print(res)

    def leave(self,  __input: list) -> None:
        slot_number = int(__input[1])

        res = self.parking_system.remove_vehicle_from_slot(slot_number)
        print(res)

    def slot_numbers_for_driver_of_age(self, __input: list) -> None:
        driver_age = int(__input[1])

        res = self.parking_system.get_slot_num_for_driver_of_age(driver_age)
        print(res)

    def slot_number_for_car_with_number(self, __input: list) -> None:
        reg_num = __input[1]

        res = self.parking_system.get_slot_num_for_car_with_num(reg_num)
        print(res)

    def vehicle_registration_number_for_driver_of_age(self, __input: list) -> None:
        driver_age = int(__input[1])

        res = self.parking_system.get_reg_num_for_driver_of_age(driver_age)
        print(res)


rif = ReadInputFile('./input.txt')
