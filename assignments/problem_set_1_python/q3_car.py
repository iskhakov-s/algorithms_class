class Car:
    def __init__(self):
        """[initializes a car with 0 speed or distance]
        """        
        self.speed = 0
        self.distance = 0

    def __str__(self):
        """[returns a string with the speed and distance]

        Returns:
            [str]: [the string]
        """        
        return ("Car: Speed = {}, Distance = {}").format(self.speed, self.distance)

    def update(self, time):
        """[increments the distance based on the time and speed]

        Args:
            time ([int]): [the amount of time the car travels at the speed]
        """        
        self.distance += self.speed * time

    @classmethod
    def from_speed(cls, spd):
        cars = cls()
        cars.speed = spd
        return cars


def main():
    truck = Car.from_speed(20)
    truck.update(10)
    truck.update(40)
    print(truck)
    # Prints:
    # Car: Speed = 20, Distance = 1000
    # (because truck drove a total of 50 time units at a speed of 20 speed units)


if __name__ == '__main__':
    main()