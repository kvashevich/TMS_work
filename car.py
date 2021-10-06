class Car:
    def __init__(self, max_speed: int) -> None:
        self.max_speed = max_speed
        self.__speed = 0
        self.__range = 0

    def get_speed(self):
        return self.__speed

    def set_speed(self, cur_speed):
        self.__speed = cur_speed
        if self.__speed > self.max_speed:
            self.__speed = self.max_speed

    speed = property(get_speed, set_speed)

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, cur_range):
        self.__range = cur_range
        if self.__range == 1000000:
            self.__range = 1000001
            print('OOOPS!')

    def move(self, hours):
        self.range += hours * self.speed

    def speed_up(self, a):
        self.speed += a

    def stop(self):
        self.speed = 0


car = Car(250)
