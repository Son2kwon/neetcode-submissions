class Node:
    key: int
    prev: Node
    next: Node
    value: int

    def __init__(self, key: int, value: int, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    d = defaultdict(int)
    head: Node
    tail: Node
    capacity: int

    def __init__(self, capacity: int):
        self.d = defaultdict(int)
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node: Node) -> Node:
        prev_node = node.prev
        next_node = node.next

        node.prev = None
        node.next = None

        prev_node.next = next_node
        next_node.prev = prev_node

        return node

    def add_to_head(self, node: Node) -> None:
        next_node = self.head.next

        node.prev = self.head
        node.next = next_node

        self.head.next = node
        next_node.prev = node

    def get(self, key: int) -> int:
        # 만약 존재한다면
        if key in self.d:
            node = self.d[key]
            node = self.remove_node(node)
            self.add_to_head(node)

            return node.value
        # 없다면 -1 반환
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # 만약 이미 존재하는 key 라면
        if key in self.d:
            # 업데이트 -> 그 부분 드러냄 -> head 쪽에 업데이트
            node = self.d[key]
            node.value = value

            node = self.remove_node(node)
            self.add_to_head(node)

            return

        # 존재하지 않는데 full 이라면
        elif len(self.d) == self.capacity:
            # tail 쪽 노드 삭제 -> 새로운 node head 쪽에 삽입
            self.d.pop(self.tail.prev.key)
            self.remove_node(self.tail.prev)

            new_node = Node(key, value)
            self.add_to_head(new_node)
            self.d[key] = new_node
        
        # 그냥 새로운 값이라면
        else:
            new_node = Node(key, value)
            self.d[key] = new_node
            self.add_to_head(new_node)


        


# get을 O(1)에 처리하기 위해선 dict
# put을 O(1)에 처리하기 위해선 double linked list