from dataclasses import dataclass

def main():
    @dataclass
    class Teams():
        teamName: str
        matchPlayed:int
        won:int
        drawn:int
        lost:int
        goalsF:int
        goalsA:int
        goalDiff:int
        points:int

    TeamArray =[ Teams("", x+1, x+1, x+1, x+1, x+1, x+1, x+1, x+1) for x in range(5)]

    data = []
    with open("testData.txt") as f:
        for line in f.readlines():
            dataL = line.strip('\n')
            dataL = dataL.split(',')

            data.append(dataL)

    x = 0
    for eaTeam in range(0, 5):
         TeamArray[eaTeam] = Teams((data[eaTeam][x]), int(data[eaTeam][x+1]), int(data[eaTeam][x+2]), int(data[eaTeam][x+3]), int(data[eaTeam][x+4]), int(data[eaTeam][x+5]), int(data[eaTeam][x+6]), int(data[eaTeam][x+7]), int(data[eaTeam][x+8]))

    displayOutputs(TeamArray)


def displayOutputs(TeamArray):
    choice = ""
    choice = input("Enter 1, 2, 3, 4, 5, or a")
    
    while choice != "5" and choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "a":
        print("Sorry that is invalid")
        choice = input("Please enter 1, 2, 3, 4, 5, or a")
    
    slot = 0

    print("Name".ljust(20) + "P".ljust(5) + "W".ljust(5) + "D".ljust(5) + "L".ljust(5) + "GF".ljust(5) + "GA".ljust(5) + "GD".ljust(5) + "Points".ljust(5))

    if choice != "a":
        slot = int(choice)
        slot = slot - 1
        print(TeamArray[slot].teamName.ljust(20) +
              str(TeamArray[slot].matchPlayed).ljust(5) +
              str(TeamArray[slot].won).ljust(5) +
              str(TeamArray[slot].drawn).ljust(5) +
              str(TeamArray[slot].lost).ljust(5) +
              str(TeamArray[slot].goalsF).ljust(5) +
              str(TeamArray[slot].goalsA).ljust(5) +
              str(TeamArray[slot].goalDiff).ljust(5) +
              str(TeamArray[slot].points))
    else:
        for x in range(0,5):
            print(TeamArray[x].teamName.ljust(20) +
                  str(TeamArray[x].matchPlayed).ljust(5) +
                  str(TeamArray[x].won).ljust(5) +
                  str(TeamArray[x].drawn).ljust(5) +
                  str(TeamArray[x].lost).ljust(5) +
                  str(TeamArray[x].goalsF).ljust(5) +
                  str(TeamArray[x].goalsA).ljust(5) +
                  str(TeamArray[x].goalDiff).ljust(5) +
                  str(TeamArray[x].points))

if __name__ == "__main__"  :
    main()

