from .robot import Robot
from .cells import EnergyCell, JumpCell, DeathCell, WarpCell
from .utils import clr, slp

class Map:
    def __init__(self, path, bot_count):
        self.start = None
        self.cells = {}
        self.extent = None
        self.time = None

        self.init_grid(path)

        self.robots = []

        for i in range(bot_count):
            self.robots.append(Robot(self, self.start, chr(ord('A') + i)))

    def init_grid(self, mpfile):
        f = open("JRMPC/maps/" + mpfile + ".txt")

        r, c, a, b, t = map(int, f.readline().split())

        self.time = t
        self.extent = (r, c)
        self.start = (a, b)

        for i in range(1, r + 1):
            ln = f.readline().split()
            
            for j in range(1, c + 1):
                elem = ln[j - 1]
                
                if elem[0] == "+":
                    self.cells[(i, j)] = JumpCell((i, j), int(elem[1:]))

                elif elem[0] == '(':
                    self.cells[(i, j)] = WarpCell((i, j), tuple(map(int, elem[1:-1].split(","))))

                elif elem[0] == 'X':
                    self.cells[(i, j)] = DeathCell((i, j))

                else:
                    self.cells[(i, j)] = EnergyCell((i, j), int(elem))

    def str_cell(self, r, c):
        ans = str(self.cells[(r, c)])

        for rb in self.robots:
            if rb.location == (r, c):
                ans += rb.identifier

        return ans + " " * (15 - len(ans))

    def draw_grid(self):
        clr()

        print("\n")

        for i in range(1, self.extent[1] + 1):
            print(*[self.str_cell(i, j) for j in range(1, self.extent[0] + 1)])
