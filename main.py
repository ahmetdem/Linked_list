class node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return self.data
    
class Linkedlist:
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            self.head = node(data=nodes.pop(0))
            current_node = self.head

            for elem in nodes:
                current_node.next = node(data=elem)
                current_node = current_node.next


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

        nodes.append("None")
        return " -> ".join(nodes)
    

    def add_first(self, node):
        node.next = self.head
        self.head = node


    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        
        for current_node in self:
            pass

        current_node.next = node


    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for current_node in self:
            if current_node.data == target_node_data:
                new_node.next = current_node.next
                current_node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)


    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head

        for current_node in self:
            if current_node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = current_node
                return

            prev_node = current_node

        raise Exception("Node with data '%s' not found" % target_node_data)
    

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        prev_node = self.head

        for current_node in self:
            if current_node.data == target_node_data:
                prev_node.next = current_node.next
                return

            prev_node = current_node

        raise Exception("Node with data '%s' not found" % target_node_data)

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head

        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next

        yield node


    def print_list(self, starting_point=None):
        nodes = []

        for node in self.traverse(starting_point):
            nodes.append(str(node))

        print(" -> ".join(nodes))   
