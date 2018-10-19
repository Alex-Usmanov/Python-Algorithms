class Node:
    value = 0
    next_ = 0

    def __init__(self, value=None, next_=None):
        self.value = value
        self.next_ = next_


class linkedList:
    __head = Node()
    __tail = Node()
    __nodes = 0

    @property
    def head(self):
        """
        Returns the head node (first) of the linked list
        """
        return self.__head

    @property
    def tail(self):
        """
        Returns the tail node (last) of the linked list
        """
        return self.__tail

    @property
    def nodes(self):
        """
        Returns the number of nodes of the linked list
        """
        return self.__nodes

    def getNode(self, index: int):
        """
        Returns the node by the given index
        """
        currentNode = self.__head

        for i in range(index):
            if currentNode.next_ == None:
                print("Node by the current index doesn't exists! Returning None")
                return None
            else:
                currentNode = currentNode.next_

        return currentNode

    def getValue(self, index: int):
        """
        Returns the value of the node by the given index
        """
        currentNode = self.__head

        for i in range(index):
            currentNode = currentNode.next_

        try:
            return currentNode.value

        except AttributeError:
            print("Node by the current index doesn't exists")

    def append(self, value):
        """
        Inserts a node with the given value to the end of the linked list
        """
        toAppend = Node(value)
        if self.__nodes == 0:
            self.__head = toAppend
            self.__tail = toAppend
            self.__head.next_ = self.__tail
        else:
            self.__tail.next_ = toAppend
            self.__tail = toAppend

        self.__nodes += 1

    def shift(self, value):
        """
        Inserts a node with the given value to the beginning of the linked list
        """
        node = Node(value)
        if self.__nodes == 0:
            self.__head = node
            self.__tail = node
            self.__head.next_ = self.__tail
        else:
            head = self.__head
            node.next_ = head
            self.__head = node
        self.__nodes += 1

    def insert(self, index: int, value):
        """
        Inserts the value AFTER index given in the function
        """
        nodeToInsert = Node(value)
        if self.__nodes == 0:
            self.__head = nodeToInsert
            self.__tail = nodeToInsert
            self.__head.next_ = self.__tail

        else:
            try:
                node = self.getNode(index)
                nodeToInsert = Node(value, node.next_.next_)
                node.next_ = nodeToInsert
            except AttributeError:
                print("Couldn't insert! Given index is too big!")

        self.__nodes += 1

    def pop(self, index=0):
        """
        Removes a node by the given index. If not specified - removes the head node
        """
        if self.nodes == 2:
            self.__head = self.__tail
        if self.nodes == 1:
            self.__head = Node(None)
            self.__tail= Node(None)
        if index == 0:
            if self.__head.next_ == self.head:
                self.__head = Node(0)
            else:
                self.__head = self.__head.next_
        else:
            previousNode = self.getNode(index-1)
            try:
                previousNode.next_ = previousNode.next_.next_
            except AttributeError:
                print("Node by given index doesn't exists")

        self.__nodes -= 1

    def replace(self, index: int, value):
        """
        Changes node's value by the given index to the given value
        """
        if index > self.__nodes - 1:
            node = self.getNode(index)
            node.value = value
