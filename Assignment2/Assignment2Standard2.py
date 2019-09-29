import math

X = [
    ["high", "vhigh", "3", "4", "medium", "high", "Q"],
    ["high", "medium", "4", "6", "small", "high", "S"],
    ["medium", "vhigh", "3", "1", "big", "medium", "S"],
    ["medium", "high", "3", "4", "big", "high", "R"],
    ["low", "high", "1", "4", "small", "low", "S"],
    ["low", "vhigh", "3", "1", "big", "medium", "Q"],
    ["low", "vhigh", "1", "6", "small", "high", "P"],
    ["low", "high", "3", "1", "medium", "low", "S"],
    ["low", "low", "4", "6", "small", "medium", "Q"],
    ["vlow", "low", "3", "1", "big", "low", "P"],
    ["vlow", "low", "6", "4", "small", "high", "S"],
    ["vlow", "low", "4", "4", "big", "medium", "R"]]

# takes list of frequencies and returns info statistic
def getInfo(list):
    sum = 0
    for i in list:
        sum += i
    temp = []
    for i in list:
        temp.append(i/sum)
    return getEntropy(temp)

# takes list of frequencies and returns entropy statistic
def getEntropy(list):
    sum = 0
    for i in list:
        if i == 0:
            sum += 0
        else:
            sum += math.log2(i) * i
    if sum == 0:
        return 0
    return sum * -1

# takes main list and returns a list of feature's value in each instance
def generateFeatureList(list, feature):
    result = []
    for i in list:
        result.append(i[feature])
    return result

# takes list of all values and returns list of each possible value
def getPossibleValues(list):
    result = []
    for i in list:
        if i not in result:
            result.append(i);
    return result

# takes list and returns list of count for each possible value
def getFrequencies(list):
    result = []
    valueList = getPossibleValues(list)
    for i in valueList:
        result.append(list.count(i))
    return result

def createSubList(list, value, feature):
    result = []
    for i in list:
        if(i[feature] == value):
            result.append(i)
    return result

def getInfoOfSubList(list):
    labelList = generateFeatureList(list, len(list[0])-1)
    freqs = getFrequencies(labelList)
    info = getInfo(freqs)
    return info

baseEntropy = getInfoOfSubList(X);
print("baseEntropy: ", baseEntropy)

ents = []

for i in range(len(X[0])-1):
    temp = generateFeatureList(X, i)
    values = getPossibleValues(temp)
    for j in values:
        a = createSubList(X, j, i)
        info = getInfoOfSubList(a)
    ents.append(info)

gains = []

for i in ents:
    gains.append(baseEntropy-i)

print(gains)
