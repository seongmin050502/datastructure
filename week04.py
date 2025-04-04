class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

# a = Node("ABC")
class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.link:
            current = current.link  # move current
        current.link = Node(data)


    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            # print(current.data)
            result = result + str(current.data) + " -> "
            current = current.link
        return result + "END"
        # return "Linked list!"


ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)
