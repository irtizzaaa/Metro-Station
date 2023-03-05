class Station:
    def __init__(self, name, line):
        self.name = name
        self.line = line

class Train:
    def __init__(self, number, line, capacity):
        self.number = number
        self.line = line
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"Passenger {passenger} boarded train {self.number}.")
        else:
            print(f"Train {self.number} is at capacity. Passenger {passenger} cannot board.")

    def remove_passenger(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            print(f"Passenger {passenger} disembarked from train {self.number}.")
        else:
            print(f"Passenger {passenger} is not on train {self.number}.") 

class MetroSystem:
    def __init__(self):
        self.stations = []
        self.trains = []

    def add_station(self, name, line):
        station = Station(name, line)
        self.stations.append(station)
        print(f"Added station {station.name} on line {station.line}.")

    def add_train(self, number, line, capacity):
        train = Train(number, line, capacity)
        self.trains.append(train)
        print(f"Added train {train.number} on line {train.line} with capacity {train.capacity}.")

    def board_train(self, passenger, line):
        for train in self.trains:
            if train.line == line and len(train.passengers) < train.capacity:
                train.add_passenger(passenger)
                return
        print(f"No available trains on line {line}. Passenger {passenger} will need to wait.")

    def disembark_train(self, passenger, train_number):
        for train in self.trains:
            if train.number == train_number:
                train.remove_passenger(passenger)
                return
        print(f"No train with number {train_number}. Passenger {passenger} is still on board.")
