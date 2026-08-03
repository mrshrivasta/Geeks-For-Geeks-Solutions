class Solution:
    def removeLoop(self, head):
        if not head or not head.next:
            return

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return

        slow = head

        if slow == fast:
            while fast.next != slow:
                fast = fast.next
            fast.next = None
            return

        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next

        fast.next = None