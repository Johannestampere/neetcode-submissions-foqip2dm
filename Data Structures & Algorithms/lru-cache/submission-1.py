class LRUCache:

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        # Dummy nodes:
        # left.next = least recently used
        # right.prev = most recently used
        self.left = self.Node(0, 0)
        self.right = self.Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev

        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]

        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])

        node = self.Node(key, value)
        self.map[key] = node
        self.insert(node)

        if len(self.map) > self.capacity:
            lru = self.left.next

            self.remove(lru)
            del self.map[lru.key]