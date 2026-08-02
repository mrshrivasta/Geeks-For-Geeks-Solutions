class Solution:
    def calc_Sum(self, arr1, arr2):
        i = len(arr1) - 1
        j = len(arr2) - 1
        carry = 0
        ans = []

        while i >= 0 or j >= 0 or carry:
            s = carry

            if i >= 0:
                s += arr1[i]
                i -= 1

            if j >= 0:
                s += arr2[j]
                j -= 1

            ans.append(str(s % 10))
            carry = s // 10

        return "".join(ans[::-1])