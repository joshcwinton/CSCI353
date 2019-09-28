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


def getAllFeatures(list, feature):
    result = [];
    for instance in list:
        result.append(instance[feature])
    return result;

def getEntropy(list):
    sum = 0
    for i in list:
        sum += math.log2(i) * i
    return sum

# Assumes all instances have same dimensionality
# def whichSplit(list):

# Need to calclulate entropy before split and average entropy after split

def printList(list):
    for i in list:
        for j in i:
            print(j, end="\t")
        print("\n")
    return 0


printList(X)
