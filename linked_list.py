

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
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
            self.size +=1



    def add(self, node):
        node.next = self.head
        self.head = node
        self.size += 1


    def append(self, node):
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
        self.size += 1


    def remove(self, target_node):
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

    def pop(self):
        node = self.tail
        return node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("End")
        return " -> ".join(nodes)

    def __len__(self):
        return self.size
        # self.size = 0
        # node = self.head
        # while node is not None:
        #     self.size += 1
        #     node = node.next
        # return self.size


if __name__ == '__main__':

    llist = LinkedList(['a', 'b', 'c'])
    llist.append(Node("z"))
    llist.add(Node("R"))
    print(llist)
    print(llist.size)
    print(len(llist))

    llist.remove(Node("b"))
    print(llist)
    print(llist.size)
    print(len(llist))
    print(llist.pop())
    # llist2 = LinkedList(["a", "b", "c", "d", "e"])
    # print()
    # print(llist2)
    # for node in llist2:
    #     print(node)
    # llist2.remove(Node("c"))
    # print(llist2)

