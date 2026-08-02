class Solution:
    def roundToNearest(self, s):
        arr = list(s)

        if arr[-1] <= '5':
            arr[-1] = '0'
            return "".join(arr)

        arr[-1] = '0'
        i = len(arr) - 2

        while i >= 0 and arr[i] == '9':
            arr[i] = '0'
            i -= 1

        if i >= 0:
            arr[i] = chr(ord(arr[i]) + 1)
            return "".join(arr)

        return "1" + "".join(arr)
        