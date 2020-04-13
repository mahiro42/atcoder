class BinaryIndexedTree:
    """Binary Indexed Treeを実装したクラス
    インデックスは1から始まることに注意すること
    """
    def __init__(self, n):
        self._size = n
        self._bit = [0] * (n + 1)

    def sum(self, i):
        """1番目からi番目までの要素の総和を返すメソッド"""
        ret = 0
        while i > 0:
            ret += self._bit[i]
            i -= i & -i
        return ret

    def add(self, i, x):
        """i番目の要素にxを加えるメソッド"""
        while i <= self._size:
            self._bit[i] += x
            i += i & -i

    def add_all(self, x):
        """BITの全要素にxを加えるメソッド"""
        for i in range(1, n + 1):
            self.add(i, x)
