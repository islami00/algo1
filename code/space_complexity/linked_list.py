
class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes: Data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        if isinstance(self.data, str) and not self.data.__contains__('\''):
            self.data = "\'%s\'" % self.data
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        """
          Returns the number of nodes in the list,
          Takes 0(n) time
          Convenience method

          :return:int
        """
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next_node
        return count

        # This is true for any except the tail node as it's next_node is none

    def prepend(self, data):
        # Since this "pseudo-insert" only involves reassignment of the head and next_node properties,
        # It is a constant time operation
        """
        Adds a new Node containing data at the head of the list
        Takes 0(1) time

        :param data: any
        :return: None
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        # This is nice because at first this method would init our tail (next_node for it is None)

    def search(self, key):
        """
        Search for the first node containing data that matches the key

        Takes 0(n)

        :param key: any
        :return: Node | None
        """
        current = self.head
        # Note: while n is not possible in term
        while current is not None:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    def insert(self, data,index : int):
        """
        Inserts a new Node containing data at index position
        Insertion takes 0(1) time but finding the node at the
        insertion point takes 0(n) time due to traversal

        Takes overall 0(n) time

        :param data: Any
        :param index: int
        :return: None
        """
        if index == 0:
            return self.prepend(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                    current = current.next_node
                    position -= 1
                # stop right before where we want to insert

            prev_node = current
            next_node = current.next_node
            # insert switcheroo
            prev_node.next_node = new
            new.next_node = next_node

    def __repr__(self):
        """
        Returns a string representation of the list
        Takes 0(n) time due to traversal.

        :return: str
        """

        nodes = []
        current = self.head

        while current is not None:
            if isinstance(current.data, str) and not current.data.__contains__('\''):
                current.data = "\'%s\'" % current.data
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:

                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '->'.join(nodes)


l = LinkedList()
l.prepend("s")
l.prepend('s')
l.prepend('s')
l.prepend('s')
l.prepend('22')
l.prepend(22)
b = l.search(22)
c = l.search('22')
d = l.search('s')
print(l)
l.insert(11,2)
print(l)
