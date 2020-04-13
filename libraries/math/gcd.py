def gcd(m, n):
    """最小公倍数を返す関数（math.gcdを使った方がよさそう）"""
    r = m % n
    return gcd(n, r) if r else n

def lcm(m, n):
    """最大公約数を返す関数"""
    return (m * n) // gcd(m, n)
