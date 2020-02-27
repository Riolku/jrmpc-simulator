from ..robot_mind import RobotMind

class Mind(RobotMind):
    def determine(self):
        return max(

            (self.getcv(self.finalpos(d)), d)

            for i in range(1, self.robot.mp.extent[0] + 1)
            for j in range(1, self.robot.mp.extent[1] + 1)

        )

    def finalpos(self, vec):
        return ((self.location[0] + vec[0] - 1) % self.robot.mp.extent[0] + 1, (self.location[1] + vec[1] - 1) % self.robot.mp.extent[1] + 1)

    def dis(self, a, b):
        dx = abs(a[0] - b[0])
        dy = abs(a[1] - b[1])

        return min(dx, self.mp.extent[0] - dx) + min(dy, self.mp.extent[1] - dy)

    def getcv(self, cell):
        return sum(

                self.robot.mp.cells[(i, j)].energy / dis(cell, (i, j))

                for i in range(1, self.robot.mp.extent[0] + 1)
                for j in range(1, self.robot.mp.extent[1] + 1)

        )
