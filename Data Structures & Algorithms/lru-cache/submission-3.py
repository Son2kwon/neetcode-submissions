class LRUCache:
    d = defaultdict(int)
    q = List[int]
    c: int
    size: int

    def __init__(self, capacity: int):
        self.d = defaultdict(int)
        self.q: List[int] = []
        self.c = capacity
        self.size = 0


    def get(self, key: int) -> int:
        if key in self.d:
            self.q.remove(key)
            self.q.append(key)
            return self.d[key]

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # 이미 존재했다면, queue 맨 뒤로 보냄 
        if key in self.d:
            self.q.remove(key)
            self.q.append(key)
            self.d[key] = value
            
            return

        self.d[key] = value
        
        if self.size == self.c:
            self.d.pop(self.q[0], None)
            self.q.remove(self.q[0])
            self.size -= 1

        self.q.append(key)
        self.size += 1


        


# get을 O(1)으로 구현하려면 dict를 사용해서 hash table을 만들어야 함
# put을 O(1)으로 구현하려면 Linked List 또는 Queue를 사용해야 함
#   Linked List로 구현한다면, 변수 head, nxt, cur 등이 필요함
#   Least used 니까, 단순히 오래되었다고 삭제하거나 하면 안 되겠네...

# Queue로 구현해서, get 할 때마다 pop한 후 다시 push
# size가 다 차면 queue[0]을 pop
#   nxt, head 등의 내용 필요 없음

# 계속 edge case가 왜 나오는거야...