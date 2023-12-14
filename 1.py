class Lamp:
    className = 'lamp'

    def __init__(self, name, power, energy_use, servise_life):
        self._name = name
        self._power = power
        self._energy_use = energy_use
        self._servise_life = servise_life

    def set_power(self, power):
        self._power = power

    def get_pover(self):
        return self._power

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def duration_of_life(self):
        return self._servise_life * 365 // 3

    def power_per_enetgyuse(self):
        return self._power / self._energy_use

    def info(self):
        print(self._name)
        print(f'power - {self._power} w')
        print(f'energy usage - {self._energy_use}')
        print(f'servise life - {self._servise_life} years')

    def __add__(self, other): # overloading add method for adding two classes
        return (self._energy_use + other._energy_use) // 2


class DaylightLamp(Lamp):
    className = 'DaylightLamp'

    def __init__(self, name, power, energy_use, servise_life, length):
        super().__init__(name, power, energy_use, servise_life)
        self.length = length

    def set_length(self, length):
        self.length = length

    def get_length(self):
        return self.length

    def info(self):
        super().info()
        print(f'length - {self.length} m')

    def ppl(self):
        return self._power/self.length


class SearchLight(Lamp):
    className = 'SearchLight'

    def __init__(self, name, power, energy_use, servise_life, weight):
        super().__init__(name, power, energy_use, servise_life)
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_weight(sefl, weight):
        self.weight = weight

    def info(self):
        super().info()
        print(f'weight - {self.weight} kg')

    def set_light_color(self, color):
        self.color = color

    def get_light_color(self):
        return self.color


lamp1 = Lamp(Lamp.className, 10, 50, 3)
lamp1.info()

lamp2 = Lamp(Lamp.className, 15, 40, 5)
print(lamp1 + lamp2)

daylight = DaylightLamp('camelion', 40, 60, 2, 1)
print(f'ppl - {daylight.ppl()}')

serl = SearchLight('main lamp', 100, 84, 6, 50)
print(f'power per enetgy use - {serl.power_per_enetgyuse()}')

print(daylight.get_pover())
print(serl.get_pover())
print(f'duration of life - {lamp1.duration_of_life()} days')

serl.set_light_color('green')
print(f'light color of {serl._name} is {serl.get_light_color()}')