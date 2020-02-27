from .map import Map
from .robot_mind import RobotMind
from importlib import import_module
from .utils import clr, slp
import JRMPC.minds

mp_name = input("Please enter the name of the map you would like to use. The required map should be named <name>.txt and placed in the maps/ folder. For example, if your map is called 'example.txt', input 'example':  ")

rcount = int(input("How many players are there?: "))

mp = Map(mp_name, rcount)

robots = mp.robots

minds = []

for i in range(rcount):
    name = input("Please input the name of the the mind you want to use to control robot '%s'. This should be the file in the minds folder. Input the file name without the .py extension and please name the class 'Mind': " % robots[i].identifier)

    minds.append(import_module("." + name, package = "JRMPC.minds").Mind(robots[i]))



for cycle in range(mp.time):
    mp.steps = mp.time - cycle
    
    for ri in range(rcount):
        if robots[ri].dead: 
            robots[ri].direction = (0, 0)
            continue

        robots[ri].direction = minds[ri].determine()

        if robots[ri].direction not in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            print("Invalid move made by robot %s! The result was %s. Not moving robot %s." % (robots[ri].identifier, robots[ri].direction, robots[ri].identifier))

            robots[ri].direction = (0, 0)


    for ri in range(rcount):
        if mp.robots[ri].direction == (0, 0): continue

        robots[ri].move(robots[ri].direction)

        mp.cells[robots[ri].location].activate(robots[ri])


    ccnts = {}

    for ri in range(rcount):
        if robots[ri].marked_cell:
            cloc = robots[ri].marked_cell.location

            ccnts[cloc] = ccnts.get(cloc, 0) + 1

    for ri in range(rcount):
        if robots[ri].marked_cell:
            cloc = robots[ri].marked_cell.location

            robots[ri].energy += mp.cells[cloc].energy / ccnts[cloc]

    for k in ccnts:
        mp.cells[k].energy = 0

    mp.draw_grid()

    slp(0.1)

print("------------------------------\nScores\n------")

l1 = []
l2 = []

for ri in range(rcount):
    l1.append(robots[ri].identifier + " " * 9)

    s = str(robots[ri].energy)

    l2.append(s + " " * (10 - len(s)))

print(*l1)
print(*l2)
