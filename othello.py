import copy

# 空白、白、黒を定義
class Stone():
    BLANK = "BLANK"
    WHITE = "WHITE"
    BLACK = "BLACK"


class Othello:
    SIZE = 8
    VECTOR = ((-1, -1), (0, -1), (1, -1), (-1, 0),
              (1, 0), (-1, 1), (0, 1), (1, 1))  # 右と下が+

    def __init__(self):
        self.SIZE
        center = self.SIZE // 2
        board = [[Stone.BLANK for i in range(self.SIZE)]
                 for j in range(self.SIZE)]  # BLANKだけの盤面boardを定義
        board[center - 1][center - 1:center + 1] = [Stone.WHITE, Stone.BLACK]
        board[center][center - 1:center + 1] = [Stone.BLACK, Stone.WHITE]
        self.board = board

    def __str__(self):
        return "\n".join(" ".join(row) for row in self.board)

    def __getitem__(self,x,y):
        return self.board[x][y]

    def copy(self, board2):  # 引数のboard2の盤面をコピーする
        self.board = copy.deepcopy(board2.board)

    # board[x][y]にstoneをおいてdx,dy方向に何個ひっくり返せるか
    def count_reversible(self, x, y, dx, dy, stone):
        count = 0
        while True:
            x += dx
            y += dy
            if not (0 <= x < self.SIZE and 0 <= y < self.SIZE):
                return 0
            if self.__getitem__(x,y) == Stone.BLANK:
                return 0
            if self.__getitem__(x,y) == stone:
                return count
            count += 1

    def judge(self, x, y, stone):  # board[x][y]にstone(WHITEorBLACK)がおけるかどうか
        if self.__getitem__(x,y)!= Stone.BLANK:
            return False
        for dx, dy in self.VECTOR:
            if self.count_reversible(x, y, dx, dy, stone) > 0:
                return True
        return False

    def put(self, x, y, stone):  # board[x][y]にstoneをおいてひっくり返す
        if not self.judge(x, y, stone):
            return False
        self.board[x][y] = stone
        for dx, dy in self.VECTOR:
            n = self.count_reversible(x, y, dx, dy, stone)  # n=ひっくり返せる数
            for i in range(1, n + 1):
                # ひっくり返せる数だけstoneに変更する
                self.board[x + dx * i][y + dy * i] = stone
        return True

    def alljudge(self, stone):  # 打てる場所を探索
        ls = []
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                if self.judge(x, y, stone):
                    ls.append((x, y))
        return ls

    def count_stone(self):
        white,black=0,0
        for x in range(8):
            for y in range(8):
                if self.__getitem__(x,y)==Stone.WHITE:
                    white+=1
                if self.__getitem__(x,y)==Stone.BLACK:
                    black+=1
        return white,black

if __name__=='__main__':
    board=Othello()
    print(board)
