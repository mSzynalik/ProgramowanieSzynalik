class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        print(f"Dom o powierzchni {self.area}, liczba pokoi {self.rooms}\n"
              f"cena domu - {self.price}zł, adres: {self.address}, pow. działki {self.plot}.")


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        print(f"Mieszkanie o powierzchni {self.area}, liczba pokoi - {self.rooms}\n"
              f"cena mieszkania: {self.price}zł. Adres - {self.address}\n"
              f"piętro - {self.floor}.")


domek = House("150 m2", 6, "500 000", "Jaworzno, Myśliwska 10", "700 m2")
mieszkanko = Flat("40 m2", 2, "250 000", "Jaworzno, Kiełbasiana 4", "4")
domek.__str__()
print()

mieszkanko.__str__()