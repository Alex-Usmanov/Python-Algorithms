from linkedList import linkedList


class queue:
    __start = 0
    __end = 0
    __linkedList = 0
    __size = 0

    def __init__(self):
        self.__linkedList = linkedList()

    @property
    def size(self):
        return self.__size

    def queue(self, toQueue):
        """
        Queues a given element
        """
        self.__linkedList.shift(toQueue)
        self.__size += 1

    def dequeue(self):
        """
        Removes the last element from the queue
        """
        nodes = self.__linkedList.nodes
        self.__linkedList.pop(nodes - 1)
        self.__size -= 1

    def front(self):
        """
        Returns the most recently added element
        """
        try:
            return self.__linkedList.head.value
        except AttributeError:
            print("The queue is empty")
    
    def back(self):
        """
        Returns the oldest element
        """
        try:
            return self.__linkedList.head.value
        except AttributeError:
            print("The queue is empty")
