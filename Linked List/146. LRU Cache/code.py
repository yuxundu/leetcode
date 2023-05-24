class Node:
    def __init__(self,key:int,val:int):
        self.key = key
        self.val = val
        self.pre=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capa = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.pre = self.left

    def remove(self, node):
        pre, nxt= node.pre, node.next
        # print("pre:",pre,"node",node.key)
        pre.next = nxt
        nxt.pre = pre

    def insert(self, node):
        pre = self.right.pre
        pre.next = node
        node.pre = pre
        node.next = self.right
        self.right.pre = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capa:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)