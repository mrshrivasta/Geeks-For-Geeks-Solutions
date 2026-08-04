class Solution:
    def makeAnagram(self, s1, s2):
        count1 = [0] * 26
        count2 = [0] * 26
        
        for c in s1:
            count1[ord(c) - ord('a')] += 1
        for c in s2:
            count2[ord(c) - ord('a')] += 1
        
        diff = 0
        for i in range(26):
            diff += max(0, count1[i] - count2[i])
        
        return diff