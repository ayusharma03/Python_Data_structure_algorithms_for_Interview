def hasSingleCycle(array):
    numElementsVisited = 0
    currenIdx = 0
    while numElementsVisited < len(array):
        if numElementsVisited > 0 and currenIdx == 0:
            return False
        numElementsVisited += 1
        currenIdx = getNextIdx(currenIdx, array)
    return currenIdx == 0

def getNextIdx(currenIdx, array):
    jump = array[currenIdx]
    nextIdx = (currenIdx + jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx +len(array)
