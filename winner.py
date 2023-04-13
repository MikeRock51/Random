#!/usr/bin/python3

def winner(matches):
    winners = []
    losers = []

    for match in matches:
        if match[0] not in winners and match[0] not in losers:
            winners.append(match[0])
        losers.append(match[1])

    absWinners = []
    for win in winners:
        if win not in losers:
            absWinners.append(win)
    
    smLosers = []
    loserDict = {}

    for los in losers:
        if los in loserDict:
            loserDict[los] += 1
        else:
            loserDict[los] = 1

    print(loserDict)

    for key, value in loserDict.items():
        if value == 1:
            smLosers.append(key)

    outList = [sorted(absWinners), sorted(smLosers)]
    return (outList)

print(winner([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
print(winner([[2,3],[1,3],[5,4],[6,4]]))
