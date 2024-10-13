# Globals for the directions
# Change the values as you see fit
EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self._instrucstions = {
            "R": self.turn_right,
            "L": self.turn_left,
            "A": self.move_forward,
        }

    @property
    def coordinates(self) -> tuple[int, int]:
        return self.x_pos, self.y_pos

    def move(self, direction: str) -> None:
        for letter in direction:
            self._instrucstions.get(letter.upper())()

    def turn_right(self) -> None:
        directions = [NORTH, EAST, SOUTH, WEST]
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def turn_left(self) -> None:
        directions = [NORTH, WEST, SOUTH, EAST]
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def move_forward(self) -> None:
        delta_x, delta_y = self.direction
        self.x_pos += delta_x
        self.y_pos += delta_y
