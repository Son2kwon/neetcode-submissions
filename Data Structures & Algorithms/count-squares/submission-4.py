class CountSquares:
    d: dict()

    def __init__(self):
        self.d = dict()

    def add(self, point: List[int]) -> None:
        x = point[0]; y = point[1]
        if (x, y) not in self.d:
            self.d[(x, y)] = 0

        x = point[0]; y = point[1];
        self.d[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        res = 0; qx = point[0]; qy = point[1];

        for x, y in self.d.keys():
            if abs(x - qx) == abs(y - qy) and x - qx != 0:
                if (x, qy) in self.d and (qx, y) in self.d:
                    res += self.d[(x, qy)] * self.d[(qx, y)] * self.d[(x, y)]

        return res
        
# duplicate는 그냥 있는 줄 알았는데, 그것까지 포함해서 세야하네
# 한 칸짜리 square 뿐 아니라 n칸짜리 square까지 세야겠네

# square가 만들어지려면
# count에서 주어진 점에서
#   같은 row에 하나 -> col이 n칸 차이라면
#   같은 col에 하나 -> row도 n칸 차이나야 하고
#   대각선에 하나 -> 현재 point에서 (-n, -n)한 자리에도 있어야 한다.
# 가 필요하다

# point를 List[int]형으로 정리한 다음에, 거기서 하나씩 찾는 건 O(n^3)의 시간 -> 음... 사악한데?

# 힌트 1: Consider the observation that can be drawn from the diagonal of a square
#   그래 BF는 O(n^3)이니까 다른 방식을 써야한다. 정사각형의 대각선에서 유래되는 관찰이라...
#   count의 point를 중심으로 하고 대각선 길이를 반지름으로 하는 원. 그 안에 있는 애들을 세는 방법..?
#   근데 이건 sqr(2)짜리는 세기 힘든데, 이건 아예 문제 조건에 없나?

# 힌트 2: (x좌표의 차이) = (y좌표의 차이)를 활용해서 diagonal endpoints를 정할 수 있다.
#   아, 주어진 점과 points에 있는 점들 중에서 (x좌표의 차이) = (y좌표의 차이)인 점들을 찾고
#   그 차이만큼 나는 점들을 찾는다? 근데 이것도 O(n^3)인데...

# 힌트 3: Hash map 사용해서 O(1) search. 대각선을 찾으면, 나머지 두 점은 어떻게 되어야 할까? (qx, qy)를 top-right으로 다뤄보자.
#   abs(dx) == abs(dy)로 대각선의 점 찾고, 두 점으로부터 dx, dy 떨어진 점 + dy, dx 떨어진 점 찾으면 되나?

# 힌트 4: 남은 두 점은 (x, qy), (qx, y)다. Counting을 할 때는 res + (count of point1) * (count of point2)
#   결국 각 점을 key로 하는 Hashmap을 작성하고
#   res += d[(x, qy)] * d[(qx, y)] 한다.
#   d는 defaultdict로 구현

# 대각선 점이 2개인 것도 세야지, dx가 0인 것도 세고

# Time Complexity: O(n); n is the number of points
# Space Complexity: O(n)