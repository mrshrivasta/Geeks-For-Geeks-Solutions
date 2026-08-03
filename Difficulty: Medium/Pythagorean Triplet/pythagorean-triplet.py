from math import isqrt

class Solution:
    def pythagoreanTriplet(self, arr):
        freq = [0] * 1001
        for x in arr:
            freq[x] += 1

        vals = [i for i in range(1, 1001) if freq[i] > 0]
        square_map = {i * i: i for i in vals}

        m = len(vals)

        for i in range(m):
            a = vals[i]
            for j in range(i, m):
                b = vals[j]
                c = square_map.get(a * a + b * b)

                if c is None or c < b:
                    continue

                if a == b:
                    if freq[a] >= 2:
                        return True
                elif b == c:
                    if freq[b] >= 2:
                        return True
                else:
                    return True

        return False