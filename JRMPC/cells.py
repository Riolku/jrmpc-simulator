class Cell:
    def __init__(self, location):
        self.location = location

    def activate(self, robot):
        raise NotImplementedError

class EnergyCell(Cell):
    def __init__(self, location, energy):
        Cell.__init__(self, location)

        self.energy = energy

    def activate(self, robot):
        robot.mark_cell(self)

    def __str__(self):
        return str(self.energy)

class JumpCell(Cell):
    def __init__(self, location, dist):
        Cell.__init__(self, location)
        
        self.distance = dist

    def activate(self, robot):
        robot.move((self.distance * robot.direction[0], self.distance * robot.direction[1]))

    def __str__(self):
        return "+%d" % self.distance

class WarpCell(Cell):
    def __init__(self, location, target):
        Cell.__init__(self, location)

        self.target = target

    def activate(self, robot):
        robot.location = self.target

    def __str__(self):
        return "(%d,%d)" % (self.target[0], self.target[1])

class DeathCell(Cell):
    def activate(self, robot):
        robot.dead = True

    def __str__(self):
        return "X"
