class SpaceAge:
    def __init__(self, seconds):
        self.earth_age = seconds / 31557600
        self.planets = {
            "mercury": 0.2408467,
            "venus": 0.61519726,
            "mars": 1.8808158,
            "jupiter": 11.862615,
            "saturn": 29.447498,
            "uranus": 84.016846,
            "neptune": 164.79132,
        }

    def on_earth(self):
        return round(self.earth_age, 2)

    def on_mercury(self):
        return self.get_age("mercury")

    def on_venus(self):
        return self.get_age("venus")

    def on_mars(self):
        return self.get_age("mars")

    def on_jupiter(self):
        return self.get_age("jupiter")

    def on_saturn(self):
        return self.get_age("saturn")

    def on_uranus(self):
        return self.get_age("uranus")

    def on_neptune(self):
        return self.get_age("neptune")

    def get_age(self, planet):
        return round(self.earth_age / self.planets.get(planet), 2)
