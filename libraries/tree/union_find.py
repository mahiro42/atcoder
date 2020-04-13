class UnionFind:
    def __init__(self, n):
        # _parents[i]: i番目のノードの親
        # _parents[i] = i ならそのノードは根
        self._parents = [i for i in range(n)]

    def get_parent(self, x):
        """ノードxの親を求めるメソッド"""
        return self._parents[x]

    def find_root(self, x):
        """ノードxの根を求めるメソッド"""
        if x == self.get_parent(x):
            return x
        else:
            # 経路圧縮を行う
            parent = self.get_parent(x)
            self._parents[x] = root = self.find_root(parent)
            return root

    def same_root(self, x, y):
        """ノードxとyの根が同じかどうかを真偽値で返すメソッド"""
        return self.find_root(x) == self.find_root(y)

    def unite(self, x, y):
        """xとyの属する集合を併合して真を返すメソッド。既に同じ集合だった場合は偽を返す"""
        root_x = self.find_root(x)
        root_y = self.find_root(y)
        if x == y:
            return False
        self._parents[y] = x
        return True
