class doubleLinkedList:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.record = {}
        self.head = doubleLinkedList(0, 0)
        self.tail = doubleLinkedList(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if(key not in self.record):
            return -1
        else:
            node = self.record[key]
            self.remove(node)
            self.add(node)
            return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if(key in self.record):
            self.remove(self.record[key])
        node = doubleLinkedList(key, value)
        self.add(node)
        self.record[key] = node
        if(len(self.record) > self.capacity):
            head = self.head.next
            self.remove(head)
            del self.record[head.key]

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)