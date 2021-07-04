class Tesla:
    # WRITE YOUR CODE HERE
    def __init__(self, model: str, color: str, autopilot: bool = False, efficiency: float = 0.3):
        self.__model = model
        self.__battery_charge = 99.9
        self.__is_locked = True
        self.__seats_count = 5
        self.__color = color
        self.__autopilot = autopilot
        self.__efficiency = efficiency
    
    @property
    def color(self):
      return self.__color
    
    @property
    def seats_count(self):
      return self.__seats_count

    @color.setter    
    def color(self, new_color:str):
      self.__color = new_color

    @seats_count.setter
    def seats_count(self, new_seat_count) ->None:
      if new_seat_count >= 2:
        self.__seats_count = new_seat_count
        print(f"The new seat count is now {new_seat_count}")


    def welcome(self) -> str:
        raise NotImplementedError

    def autopilot(self, obstacle: str) -> str:
        # COMPLETE THE FUNCION
        if self.__autopilot:
            return f"Tesla model {self.__model} avoids {obstacle}"
        return "Autopilot is not available"

    def lock(self):
      self.__is_locked = True

    def unlock(self):
      self.__is_locked = False
  
    def open_doors(self) -> str:
        if self.__is_locked:
          return "Car is locked!"
        return "Doors opens sideways"

    def check_battery_level(self) -> str:
        return f"Battery charge level is {self.__battery_charge}%"
 
    def charge_battery(self):
        self.__battery_charge = 100
        self.check_battery_level()

    def drive(self, travel_range: float):
        battery_discharge_percent = travel_range * self.__efficiency
        if self.__battery_charge - battery_discharge_percent >= 0:
          self.__battery_charge = (self.__battery_charge - battery_discharge_percent)
        return self.check_battery_level()
