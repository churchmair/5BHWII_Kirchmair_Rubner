import random
from linkedList import LinkedList

if __name__ == '__main__':

    ll = LinkedList()
    for i in range(15):
        ll.append(random.randint(1, 100))
    print("list:")
    ll.printList()

    # print length
    print("length:")
    print(ll.getLength())

    # use the iterator
    print("iterator:")
    for node in ll:
        print(node)
