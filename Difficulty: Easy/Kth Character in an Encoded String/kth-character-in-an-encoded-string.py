class Solution:
    def decodeIt(self, s, k):
        ops = []
        i = 0
        n = len(s)
        while i < n:
            if s[i].isdigit():
                ops.append(('mult', int(s[i])))
            else:
                ops.append(('char', s[i]))
            i += 1
        
        lengths = []
        length = 0
        for op in ops:
            if op[0] == 'char':
                length += 1
            else:
                length *= op[1]
            lengths.append(length)
        
        idx = len(ops) - 1
        cur_k = k
        while idx >= 0:
            op = ops[idx]
            prev_length = lengths[idx - 1] if idx > 0 else 0
            if op[0] == 'mult':
                cur_k = ((cur_k - 1) % prev_length) + 1
                idx -= 1
            else:
                if cur_k == prev_length + 1:
                    return op[1]
                else:
                    idx -= 1
        
        return ''