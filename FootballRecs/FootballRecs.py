from dataclasses import dataclass
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

def displayOutputs(teamArray):
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
        print(teamArray[slot].teamName.ljust(20) +
              str(teamArray[slot].matchPlayed).ljust(5) +
              str(teamArray[slot].won).ljust(5) +
              str(teamArray[slot].drawn).ljust(5) +
              str(teamArray[slot].lost).ljust(5) +
              str(teamArray[slot].goalsF).ljust(5) +
              str(teamArray[slot].goalsA).ljust(5) +
              str(teamArray[slot].goalDiff).ljust(5) +
              str(teamArray[slot].points))
    else:
        for x in range(0,5):
            print(teamArray[x].teamName.ljust(20) +
                  str(teamArray[x].matchPlayed).ljust(5) +
                  str(teamArray[x].won).ljust(5) +
                  str(teamArray[x].drawn).ljust(5) +
                  str(teamArray[x].lost).ljust(5) +
                  str(teamArray[x].goalsF).ljust(5) +
                  str(teamArray[x].goalsA).ljust(5) +
                  str(teamArray[x].goalDiff).ljust(5) +
                  str(teamArray[x].points))



def getFootballData(teamArray):
    data = []
    with open("testData.txt") as f:
        for line in f.readlines():
            dataL = line.strip('\n')
            dataL = dataL.split(',')

            data.append(dataL)
    print(data)
    x = 0
    for eaTeam in data:
        singleTeam = Teams("",0,0,0,0,0,0,0,0)
        singleTeam.teamName = eaTeam[0]
        singleTeam.matchPlayed = eaTeam[1]
        singleTeam.won = eaTeam[2]
        singleTeam.drawn = eaTeam[3]
        singleTeam.lost = eaTeam[4]
        singleTeam.goalsF = eaTeam[5]
        singleTeam.goalsA = eaTeam[6]
        singleTeam.goalDiff = eaTeam[7]
        singleTeam.points = eaTeam[8]
        teamArray.append(singleTeam)
    return(teamArray)

def main():
    teamArray = []
    teamArray = getFootballData(teamArray)
    displayOutputs(teamArray)
    
    
if __name__ == "__main__"  :
    main()

