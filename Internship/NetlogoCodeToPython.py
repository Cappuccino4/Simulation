import csv
import random

#######################################
#Globals
listOfBasicAgents = []
listOfDissAgents = []
listOfSpokespersons = []
listOfFlowManipulators = []
listOfLiveAgents = []
listOfPhysicalEventAgents = []
listOfIPS = []
matrix = []
allAgents = []

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
        self.IPs = []

    def addIP(self, IPNumber):
        if IPNumber not in self.IPs:
            self.IPs.append(IPNumber)

    def getIP(self):
        if len(self.IPs) > 0:
            num = random.randrange(len(self.IPs))
            return self.IPs[num]

    def __str__(self):
        return f"{self.id}, {self.country}, {self.gender}, {self.age}, {self.language}, {self.nationality}, {self.politicalSpectrum}, {self.socioeconomicStatus}, {self.eu}, {self.natoRussia}, {self.xCord}, {self.yCord}, {self.IPs}"

class InformationDissAgent():
    def __init__(self, size, id, agentType, relatedIP, stance, topicID):
        self.size = size
        self.id = id
        self.agentType = agentType
        self.relatedIP = relatedIP
        self.stance = stance
        self.topicID = topicID

    def getIP(self):
        return self.relatedIP

    def addIP(self, IP):
        return 0

    def __str__(self):
        return f"{self.size}, {self.id}, {self.agentType}, {self.relatedIP}, {self.stance}, {self.topicID}"

class NBSpokespersonAgent():
    def __init__(self, size, id, agentType):
        self.size = size
        self.id = id
        self.agentType = agentType

    def __str__(self):
        return f"{self.size}, {self.id}, {self.agentType}"

class NBFlowManipulatorAgent():
    def __init__(self, size, id, agentType):
        self.size = size
        self.id = id
        self.agentType = agentType

    def __str__(self):
        return f"{self.size}, {self.id}, {self.agentType}"

class NBLiveAgent():
    def __init__(self, size, id, agentType):
        self.size = size
        self.id = id
        self.agentType = agentType

    def __str__(self):
        return f"{self.size}, {self.id}, {self.agentType}"

class NBPhysicalEventAgent():
    def __init__(self, size, id, agentType, relatedIP, stance, topicID):
        self.size = size
        self.id = id
        self.agentType = agentType
        self.relatedIP = relatedIP
        self.stance = stance
        self.topicID = topicID

    def __str__(self):
        return f"{self.size}, {self.id}, {self.agentType}, {self.relatedIP}, {self.stance}, {self.topicID}"

class IP():
    def __init__(self, size, id, type, relatedTopicID, IPID):
        self.size = size

        self.id = id
        self.type = type
        self.relatedTopicID = relatedTopicID
        self.IPID = IPID

    def __str__(self):
        return f"{self.size}, {self.id}, {self.type}, {self.relatedTopicID}, {self.IPID}"

def createBasicAgents(agentNum):
    with open("potato.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if (line_count >= agentNum + 2):
                break
            if line_count == 0 or line_count == 1:
                line_count += 1
            else:
                listOfBasicAgents.append(BasicAgent(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], random.randint(0, 100), random.randint(0, 100)))
                line_count += 1

def createNBInformationDissAgents(num):
    with open("information-diss-agents-input.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        lineCount = 0
        for row in csv_reader:
            if lineCount >= num:
                break
            listOfDissAgents.append(InformationDissAgent(row[0], row[1], row[2], row[3], row[4], row[5]))
            lineCount += 1

def createNBSpokespersonAgents(num):
    with open("spokesperson-agents-input.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        lineCount = 0
        for row in csv_reader:
            if lineCount >= num:
                break
            listOfSpokespersons.append(NBSpokespersonAgent(row[0], row[1], row[2]))
            lineCount += 1

def createNBFlowManipulatorAgents(num):
    with open("flow-manipulator-agents-input.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        lineCount = 0
        for row in csv_reader:
            if lineCount >= num:
                break
            listOfFlowManipulators.append(NBFlowManipulatorAgent(row[0], row[1], row[2]))
            lineCount += 1

def createNBLiveAgents(num):
    with open("live-agents-input.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        lineCount = 0
        for row in csv_reader:
            if lineCount >= num:
                break
            listOfLiveAgents.append(NBLiveAgent(row[0], row[1], row[2]))
        lineCount += 1

def createNBPhysicalEventAgents(num):
    with open("physical-event-agent-input.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        lineCount = 0
        for row in csv_reader:
            if lineCount >= num:
                break
            listOfPhysicalEventAgents.append(NBPhysicalEventAgent(row[0], row[1], row[2], row[3], row[4], row[5]))
        lineCount += 1

def createIP(num):
    with open("IPs-input.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        lineCount = 0
        for row in csv_reader:
            if lineCount >= num:
                break
            listOfIPS.append(IP(row[0], row[1], row[2], row[3], row[4]))
        lineCount += 1

def generateMatrix(sum):
    with open("Example_adjacency_matrix_1000.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        lineCount = 0
        for row in csv_reader:
            arr = []
            rowCount = 0
            if lineCount >= sum:
                break
            for i in row:
                if rowCount >= sum:
                    break
                arr.append(i)
                rowCount += 1
            matrix.append(arr)
            lineCount += 1

def getAgents(basic, diss):
    createBasicAgents(basic)
    createNBInformationDissAgents(diss)
    generateMatrix(basic+diss)

def sendDissInfromation():
    for i in range(len(allAgents)):
        if type(allAgents[i]) is InformationDissAgent:
            row = matrix[i]
            count = 0
            for j in row:
                if j == "1":
                    sendIP(i, count)
                count += 1

def sendIP(dissAgentNum, basicAgentNum):
    dissAgent = allAgents[dissAgentNum]
    basicAgent = allAgents[basicAgentNum]
    if not dissAgent.getIP() == None:
        basicAgent.addIP(dissAgent.getIP())

def createAllAgentList():
    for i in range(len(listOfBasicAgents)):
        allAgents.append(listOfBasicAgents[i])
    for i in range(len(listOfDissAgents)):
        allAgents.append(listOfDissAgents[i])

def sendAllInformation():
    for i in range(len(allAgents)):
        if type(allAgents[i]) is BasicAgent:
            row = matrix[i]
            count = 0
            for j in row:
                if j == "1":
                    sendIP(i, count)
                count += 1

def main():
    getAgents(995, 5)
    createAllAgentList()
    for i in range(5):
        if i == 0:
            sendDissInfromation()
        else:
            sendAllInformation()

main()
print(allAgents[989])

##If you want to see the code work, just use print(allAgents[94]) or whatever value you would like!