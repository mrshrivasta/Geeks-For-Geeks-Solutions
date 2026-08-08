class Solution:
    def countTabs(self, arr):
        open_tabs = set()

        for x in arr:
            if x == "END":
                open_tabs.clear()
            elif x in open_tabs:
                open_tabs.remove(x)
            else:
                open_tabs.add(x)

        return len(open_tabs)