
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        distinctNode = currentNode.next
        while distinctNode is not None and currentNode.value == distinctNode.value:
            distinctNode = distinctNode.next
        currentNode.next = distinctNode
        currentNode = distinctNode
    return linkedList
