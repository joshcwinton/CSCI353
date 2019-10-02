# JOSH WINTON

# Code for Standard 2 of Assignment 2 in CSCI 353

# Takes in a dataset of instances with features in x[0] through x[n-1] and labels
# in x[n] and returns which feature should be split on based in information gain statistic

import math

dataset = [
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

# Generate weighted info statistic for a list of frequencies
def getWeightedInfo(list, weight):
    info = getInfo(list)
    sum = 0
    for i in list:
        sum += i
    if weight != 0:
        return (sum/weight) * info
    else:
        return 0

# takes list of frequencies and returns info statistic
def getInfo(list):
    sum = 0
    for i in list:
        sum += i
    temp = []
    for i in list:
        temp.append(i / sum)
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

# takes list of instance and returns a list of the feature's value in each instance
def generateFeatureList(list, feature):
    result = []
    for i in list:
        result.append(i[feature])
    return result

# takes list of values and returns list of each possible value once
def getPossibleValues(list):
    result = []
    for i in list:
        if i not in result:
            result.append(i)
    return result

# takes list and returns list of count for each possible value, in matching order
def getFrequencies(list):
    result = []
    valueList = getPossibleValues(list)
    for i in valueList:
        result.append(list.count(i))
    return result

# takes list of instances, searches for value at feature number and returns list of instances that match
def createSubList(list, value, feature):
    result = []
    for i in list:
        if(i[feature] == value):
            result.append(i)
    return result

# Takes a list, returns its information, based on label in the last feature/index
def getInfoOfSubList(list):
    labelList = generateFeatureList(list, len(list[0]) - 1)
    freqs = getFrequencies(labelList)
    info = getInfo(freqs)
    return info

# Gets info but info of each node is weighted based on instances that reach it
def getWeightedInfoOfSubList(list, weight):
    labelList = generateFeatureList(list, len(list[0]) - 1)
    freqs = getFrequencies(labelList)
    info = getWeightedInfo(freqs, weight)
    return info

baseInfo = getInfoOfSubList(dataset)
print(f"Base info:\t{baseInfo}")

gains = []

for feature in range(0, 6):
    sum = 0
    for value in getPossibleValues(generateFeatureList(dataset, feature)):
        subList = createSubList(dataset, value, feature)
        sum += getWeightedInfoOfSubList(subList, len(dataset))
    gain = baseInfo - sum
    gains.append(gain)

for i in range(len(gains)):
    print(f'Gain({i+1}): \t{gains[i]}')

highestGain = max(gains)
splitOn = gains.index(highestGain)

print(f'Highest Gain:\t{highestGain}')
print(f'Split on feature number {splitOn+1}')
