import random

class Door:
    def __init__(self, num, object):
        self.num = num
        self.object = object

numberOfWins = 0

timesToRun = input("Iterations to run:")

for j in range (0, int(timesToRun)):
    doors = [Door(1, "car"), Door(2, "car"), Door(3, "car")]
    holdDoors = [Door(1, "n/a"), Door(2, "n/a"), Door(3, "n/a")]

    i = 0

    while i < 2:
        door = random.choice(holdDoors)
        doorNum = door.num - 1
        doors[doorNum].object = "goat"
        holdDoors.remove(door)
        i += 1

    chosenDoor = random.choice(doors)
    doorNum = chosenDoor.num

    openedDoor = Door(0, "hold")

    if doors[0].object is "goat" and doors[0].num != doorNum:
        openedDoor = doors[0]
    elif doors[1].object is "goat" and doors[1].num != doorNum:
        openedDoor = doors[1]
    else:
        openedDoor = doors[2]

    print("Your Door, door number", doorNum, ":", chosenDoor.object)

    print("Door 1: ", doors[0].object)
    print("Door 2: ", doors[1].object)
    print("Door 3: ", doors[2].object)

    newChosenDoor = Door(99, 'n/a')

    for door in doors:
        if door.num != doorNum and door.num != openedDoor.num:
            newChosenDoor = door



    if newChosenDoor.object is "car":
        print("WIN")
        numberOfWins += 1

    print("////////////////////////////////////////////////////////////////")

winPercent = (numberOfWins/int(timesToRun)) * 100

print("Simulated ", timesToRun, " iterations of the Monty Hall Problem", sep="")
print("Win Percentage: ", winPercent, "%", sep='')