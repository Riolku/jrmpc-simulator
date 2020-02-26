class Robot:
    def __init__(self, mp, location, ident):
        self.mp = mp
        self.location = location
        self.energy = 0
        self.dead = False
        self.direction = None
        self.identifier = ident
        self.marked_cell = None

    def move(self, direction):
        self.location = (
                (self.location[0] + direction[0] - 1) % self.mp.extent[0] + 1,
                (self.location[1] + direction[1] - 1) % self.mp.extent[1] + 1
        )

    def mark_cell(self, cell):
        self.marked_cell = cell
