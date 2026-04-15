class Tromino1:
    def __init__(self, n=3, x=0, y=0):
        self.tno = 0
        self.size = 2**n
        self.map = [['x' if i == x and j == y else '0' for j in range(self.size)] for i in range(self.size)]
        
        if not self.isValid(x, y, 0, 0, self.size-1, self.size-1):
            print("Invalid input tile")
        else:
            print("[초기 맵 상태]")
            self.printMap()
            
            # 파라미터 순서: n, startX, endX, startY, endY, x, y
            self.solve(n, 0, self.size-1, 0, self.size-1, x, y)
            
            print("[해결된 맵 상태]")
            self.printMap()

    def solve(self, n, startX, endX, startY, endY, x, y):
        # 맵 크기가 1x1이 되면 종료
        if n == 0:
            return

        cx, cy = self.getCenter(startX, endX, startY, endY)

        # 4분면의 중심에 배치될 가상의 빈칸 좌표 세팅
        x1, y1 = cx, cy             # 1사분면 (Top-Left)
        x2, y2 = cx, cy + 1         # 2사분면 (Top-Right)
        x3, y3 = cx + 1, cy         # 3사분면 (Bottom-Left)
        x4, y4 = cx + 1, cy + 1     # 4사분면 (Bottom-Right)

        # 실제 빈칸(x, y)이 위치한 사분면 파악 및 중앙에 트로미노(L자) 1개 배치
        if x <= cx:
            if y <= cy:
                # 빈칸이 1사분면에 있음 -> 2, 3, 4사분면 중앙을 블록으로 채움
                self.placeTiles(x2, y2, x3, y3, x4, y4)
                x1, y1 = x, y
            else:
                # 빈칸이 2사분면에 있음
                self.placeTiles(x1, y1, x3, y3, x4, y4)
                x2, y2 = x, y
        else:
            if y <= cy:
                # 빈칸이 3사분면에 있음
                self.placeTiles(x1, y1, x2, y2, x4, y4)
                x3, y3 = x, y
            else:
                # 빈칸이 4사분면에 있음
                self.placeTiles(x1, y1, x2, y2, x3, y3)
                x4, y4 = x, y

        # 더 이상 쪼갤 수 없으면 재귀 종료
        if n == 1:
            return
        else:
            # 4개의 사분면으로 나누어 각각 재귀 호출 (경계값 분리: cx+1, cy+1 사용)
            self.solve(n-1, startX, cx, startY, cy, x1, y1)         # 1사분면
            self.solve(n-1, startX, cx, cy+1, endY, x2, y2)         # 2사분면
            self.solve(n-1, cx+1, endX, startY, cy, x3, y3)         # 3사분면
            self.solve(n-1, cx+1, endX, cy+1, endY, x4, y4)         # 4사분면
            
    def placeTiles(self, x1, y1, x2, y2, x3, y3):
        self.tno += 1
        self.map[x1][y1] = self.tno
        self.map[x2][y2] = self.tno
        self.map[x3][y3] = self.tno

    def getCenter(self, startX, endX, startY, endY):
        return ((startX + endX) // 2, (startY + endY) // 2)
    
    def printMap(self):
        for i in range(self.size):
            for j in range(self.size):
                print("{:<3}".format(self.map[i][j]), end='')
            print()
        print()

    def isValid(self, x, y, startX, startY, endX, endY):
        return (startX <= x <= endX) and (startY <= y <= endY)

# 실행 예시: 2^3 x 2^3 (8x8) 크기 맵에 시작 빈칸이 (1, 2)인 경우
# Tromino(3, 1, 2)