class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def printList(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next

    def getLength(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def __iter__(self):
        cur_node = self.head
        while cur_node:
            yield cur_node.value
            cur_node = cur_node.next

    def calcAverage(self):
        cur_node = self.head
        sum = 0
        while cur_node:
            sum += cur_node.value
            cur_node = cur_node.next
        calc_average = sum / self.getLength()
        print(f"sum: {sum} at a lengt of: {self.getLength()}")
        return calc_average
