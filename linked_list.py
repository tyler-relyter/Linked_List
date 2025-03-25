# AUTHORED_BY:  Tyler Bullard
# COURSE:       CSC 231-001
# ASSIGNMENT:   HW2
# DUE_DATE:     3/28/2025
# DESCRIPTION: This file contains the Node and LinkedList classes, used to implement the Linked List ADT.

class Node:
    def __init__(self, data=None) -> None:
        """
        Constructor for Node class
        :param data: Any
        """
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        """
        Returns the data of the node
        :return: Any
        """
        return str(self.data)


class LinkedList:
    def __init__(self, nodes=None) -> None:
        """
        Constructor for LinkedList class
        :param nodes: List, optional
        """
        self.head = None
        self.tail = None
        self.size = 0
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for el in nodes:
                node.next = Node(data=el)
                node = node.next
                self.size += 1
            self.tail = node
            self.size += 1

    def add(self, item) -> None:
        """
        Adds a node to the front of the linked list
        :param item: Any
        :return: None
        """
        node = Node(item)
        node.next = self.head
        self.head = node
        self.size += 1
        return

    def append(self, item) -> None:
        """
        Adds a node to the end of the linked list
        :param item: Any
        :return: None
        """
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node
        self.tail = node
        self.tail.next = None
        self.size += 1
        return

    def search(self, item) -> bool:
        """
        Searches for a node in the linked list
        :param item: Any
        :return: bool
        """
        target_node = Node(item)
        if self.head is None:
            raise Exception("Error: Linked List is empty")
        if self.head.data == target_node.data:
            return True
        for node in self:
            if node.data == target_node.data:
                return True
        return False

    def remove(self, item) -> None:
        """
        Removes a node from the linked list
        :param item: Any
        :return: None
        """
        target_node = Node(item)
        if self.head is None:
            raise Exception("Error: Linked List is empty")
        if self.head.data == target_node.data:
            self.head = self.head.next
            self.size -= 1
            return
        prev_node = self.head
        for node in self:
            if node.data == target_node.data:
                prev_node.next = node.next
                self.size -= 1
                return
            prev_node = node
        raise Exception(f"{target_node.data} not found in LinkedList")

    def pop(self, pos=None) -> Node:
        """
        Removes and returns the last node in the linked list if no position is given. Otherwise, removes and returns the
        node at the given position.
        :param pos: int, optional
        :return: Node
        """
        if self.head is None:
            raise Exception("Error: Linked List is empty")
        if pos is None:
            if self.head == self.tail:  # If only one node exists
                popped_node = self.head
                self.head = self.tail = None
                self.size -= 1
                return popped_node
            prev_node = self.head
            while prev_node.next != self.tail:
                prev_node = prev_node.next
            popped_node = self.tail
            prev_node.next = None
            self.tail = prev_node
            self.size -= 1
            return popped_node

            # Pop at a specific position
        if not isinstance(pos, int):
            raise ValueError("Parameter 'pos' must be of type: int")
        if pos < 0 or pos >= self.size:
            raise IndexError(f"Given index {pos} is out of range: List contains {self.size} objects")

            # Pop head node
        if pos == 0:
            popped_node = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return popped_node

        prev_node = self.head
        for _ in range(pos - 1):
            prev_node = prev_node.next
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        if popped_node == self.tail:
            self.tail = prev_node
        self.size -= 1
        return popped_node

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty
        :return: bool
        """
        return self.size == 0

    def __iter__(self) -> Node:
        """
        Iterates through the linked list
        :yield: Node
        """
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        """
        Returns the linked list as a string
        :return: str
        """
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("End")
        return " -> ".join(nodes)

    def __len__(self) -> int:
        """
        Returns the size of the linked list
        :return: int
        """
        return self.size


if __name__ == '__main__':
    llist = LinkedList(['a', 'b', 'c'])
    print(llist)
    print(llist.pop())
    print(llist.pop())
    print(llist.pop())
    print(llist)
    print(llist.size)
    llist.append("z")
    llist.add("R")
    print(llist)
    print(llist.size)
