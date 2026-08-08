class Solution:
    def matchPairs(self, nuts, bolts):
        order = ['!', '#', '$', '%', '&', '*', '?', '@', '^']
        rank = {ch: i for i, ch in enumerate(order)}

        nuts.sort(key=lambda x: rank[x])
        bolts.sort(key=lambda x: rank[x])