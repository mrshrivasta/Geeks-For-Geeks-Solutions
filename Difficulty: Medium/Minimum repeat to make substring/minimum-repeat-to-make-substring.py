class Solution:
    def minRepeats(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        count = -(-n2 // n1)  # ceiling division
        repeated = s1 * count
        
        if s2 in repeated:
            return count
        
        repeated += s1
        count += 1
        if s2 in repeated:
            return count
        
        return -1