def findMostCommon(strings):
    smallestString = getSmallest(strings)
    commonChars = set(smallestString)

    for string in strings:
        removeChars(string, commonChars)

    return "".join(list(commonChars))

def getSmallest(strings):
    result = strings[0]

    for string in strings[1:]:
        if len(string) < len(result):
            result = string

    return result

def removeChars(string, commonChars):
    uniqueChars = set(string)

    for char in list(commonChars):
        if char not in uniqueChars:
            commonChars.remove(char)

strs = ["flower","flow","flight"]
res = findMostCommon(strs)
print(res)
