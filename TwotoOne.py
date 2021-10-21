def longest(a1, a2):
    finalList = []
    for eaVal in a1:
        count1 = finalList.count(eaVal)
        if count1 == 0:
            finalList.append(eaVal)
    for eaVal in a2:
        count1 = finalList.count(eaVal)
        if count1 == 0:
            finalList.append(eaVal)
    finalList.sort()
    return ''.join(finalList)


a1 = input("Enter a string:")
a2 = input("Enter another string:")
print("Here are the original strings:")
print(a1)
print(a2)
print("")
print("The two strings sorted have been put together to form the longest possible list, without repeating a letter:")
print(longest(a1, a2))
