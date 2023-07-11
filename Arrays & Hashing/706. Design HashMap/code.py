class ListNode:
    def __init__(self,key=-1,value=-1,next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for i in range(1000)]
        
    def put(self, key: int, value: int) -> None:
        index = key%1000
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = ListNode(key,value)
        

    def get(self, key: int) -> int:
        
        index = key%1000
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        index = key%1000
        cur = self.map[index]

        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next

                return
            cur = cur.next

        



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)