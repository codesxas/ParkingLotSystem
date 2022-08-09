class Vehicle:
    """
        Vehicle: An object to store details related to Vehicle.
        includes 
            driver's age (driver_age),
            registration number (registration_number)
    """
    def __init__(self, age: int, reg_num: str) -> None:
        self.driver_age = age
        self.registration_number = reg_num

    def __repr__(self):
        return f"Driver's age = {self.driver_age}, " \
               f"Registration Number = '{self.registration_number}'"
