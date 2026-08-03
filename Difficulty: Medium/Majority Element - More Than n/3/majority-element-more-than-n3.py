class Solution:
    def findMajority(self, arr):
        cand1 = cand2 = None
        cnt1 = cnt2 = 0

        for num in arr:
            if cand1 == num:
                cnt1 += 1
            elif cand2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                cand1 = num
                cnt1 = 1
            elif cnt2 == 0:
                cand2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = cnt2 = 0
        for num in arr:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1

        ans = []
        n = len(arr)

        if cnt1 > n // 3:
            ans.append(cand1)
        if cnt2 > n // 3:
            ans.append(cand2)

        ans.sort()
        return ans