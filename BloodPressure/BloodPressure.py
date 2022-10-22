from dataclasses import dataclass

def processOutcomes(readings, outcomes):
    for eaPatient in range(0,10):
        if readings[eaPatient].diastolic < 60 and readings[eaPatient].systolic < 90:
            outcomes.append("Low")
        elif readings[eaPatient].diastolic < 80 and readings[eaPatient].systolic < 120:
            outcomes.append("Ideal")
        elif readings[eaPatient].diastolic < 90 and readings[eaPatient].systolic < 140:
            outcomes.append("Pre-High")
        else:
            outcomes.append("High")


def writeResults(readings, outcomes):
    f = open("results.txt", "w")
    for eaPatient in range(0, 10):
        f.write(readings[eaPatient].patientName +  ": " + outcomes[eaPatient] + "\n")
    f.close()


def main():
    @dataclass
    class Reading():
        patientName:str
        systolic:int
        diastolic:int
        
    readingArray =[ Reading("", x+1, x+1) for x in range(10)]
    outcomes = []
    data = []

    with open("data.txt") as f:
        for line in f.readlines():
            dataL = line.strip('\n')
            dataL = dataL.split(',')

            data.append(dataL)

    x = 0
    for eaPatient in range(0, 10):
        readingArray[eaPatient] = Reading((data[eaPatient][x]), int(data[eaPatient][x+1]), int(data[eaPatient][x+2]))


    processOutcomes(readingArray, outcomes)
    writeResults(readingArray, outcomes)

if  __name__ == "__main__" :
    main()

