from ..robot_mind import RobotMind

class Mind(RobotMind):
    def determine(self):
        self.robot.mp.draw_grid()

        print("\nYou are robot " + self.robot.identifier)

        dr = None

        while dr not in ["up", "down", "left", "right"]:
            dr = input("Please input a direction (one of 'up', 'down', 'left' or 'right'): ").lower().strip()

        return [(-1, 0), (1, 0), (0, -1), (0, 1)][["up", "down", "left", "right"].index(dr)]
