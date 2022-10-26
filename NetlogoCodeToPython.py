import csv
import random

#######################################
#Globals
listOfBasicAgents = []
listOfDissAgents = []

#######################################

class BasicAgent():
    def __init__(self, id, country, gender, age, language, nationality, politicalSpectrum, socioeconomicStatus, eu, natoRussia, xCord, yCord):
        self.id = id
        self.country = country
        self.gender = gender
        self.age = age
        self.language = language
        self.nationality = nationality
        self.politicalSpectrum = politicalSpectrum
        self.socioeconomicStatus = socioeconomicStatus
        self.eu = eu
        self.natoRussia = natoRussia
        self.xCord = xCord
        self.yCord = yCord

    def __str__(self):
        return f"{self.id}, {self.country}, {self.gender}, {self.age}, {self.language}, {self.nationality}, {self.politicalSpectrum}, {self.socioeconomicStatus}, {self.eu}, {self.natoRussia}, {self.xCord}, {self.yCord}"

class InformationDissAgent():
    def __init__(self, size, id, agentType, relatedIP, stance, topicID):
        self.size = size
        self.id = id
        self.agentType = agentType
        self.relatedIP = relatedIP
        self.stance = stance
        self.topicID = topicID

    def __str__(self):
        return f"{self.size}, {self.id}, {self.agentType}, {self.relatedIP}, {self.stance}, {self.topicID}"

def createBasicAgents():
    with open("potato.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0 or line_count == 1:
                line_count += 1
            else:
                listOfBasicAgents.append(BasicAgent(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], random.randint(0, 100), random.randint(0, 100)))
                line_count += 1

def createNBInformationDissAgents():
    with open("information-diss-agents-input.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            listOfDissAgents.append(InformationDissAgent(row[0], row[1], row[2], row[3], row[4], row[5]))

def createNBSpokespersonAgents():
    print("Hello")

def createNBFlowManipulatorAgents():
    print("Hello")

def createNBLiveAgents():
    print("Hello")

def createNBPhysicalEventAgents():
    print("Hello")

createBasicAgents()
createNBInformationDissAgents()
