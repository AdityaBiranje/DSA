class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        def merge(l1, l2):
            dummy = ListNode(0)
            curr = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next

                curr = curr.next

            curr.next = l1 if l1 else l2

            return dummy.next

        interval = 1

        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = merge(lists[i], lists[i + interval])

            interval *= 2

        return lists[0]