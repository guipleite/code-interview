def nth_to_last(head,k): 

    if head != None:
        p1 = head

        for i in range(k):
            if head != None:
                head = head.next
            else:
                return

        p2 = head

        while p2 != None:
            p1 = p1.next
            p2 = p2.next

        return p1
