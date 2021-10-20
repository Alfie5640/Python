teamName = input("What is the name of the team?")
teamScores = [4, 5, 6]
numOfTries = input("How many tries did " + str(teamName) + " get?")
while int(numOfTries) < 0:
    numOfTries = input("You must have 0 or more tries... Please try again:")

numOfConversions = input("How many conversions did " + teamName + " get?")
while int(numOfConversions) < 0:
    numOfConversions = input("You must have 0 or more conversions... Please try again:")

numOfPenalties = input("How many penalties did " + teamName + " get?")
while int(numOfPenalties) < 0:
    numOfPenalties = input("You must have 0 or more penalties... Please try again:")

numOfDropGoals = input("How many drop-goals did " + teamName + " get?")
while int(numOfDropGoals) < 0:
    numOfDropGoals = input("You must have 0 or more drop goals... Please try again:")

print(teamName.upper() + " scored:\n tries: " + numOfTries + "\n conversions: " + numOfConversions)

print(" penalties: " + numOfPenalties + "\n drop-goals: " + numOfDropGoals)

finalScore = (5 * int(numOfTries)) + (2 * int(numOfConversions)) + (3 * int(numOfPenalties)) + (3 * int(numOfDropGoals))

print(" total points achieved: " + str(finalScore) + "\n")
for eaInt in range(0, int(numOfDropGoals)):
    print("You got a drop goal!")

teamScores.append(finalScore)
print("\nTeam Scores")
print("-----------")
for eaVal in teamScores:
    if eaVal == finalScore:
        print(str(eaVal))
    else:
        print(str(eaVal), end=", ")
print("-----------")
