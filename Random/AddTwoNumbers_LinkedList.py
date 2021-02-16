class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLinkedList(l: ListNode) -> None:
    if l:
        print(l.val, end=" ")
        nextNode = l.next
        while nextNode:
            print(nextNode.val, end=" ")
            nextNode = nextNode.next
        print()



def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    results = []
    carry_forward = 0
    while l1 is not None or l2 is not None or carry_forward != 0:
        first_digit = l1.val if l1 is not None else 0
        second_digit = l2.val if l2 is not None else 0
        sum_digit = first_digit + second_digit + carry_forward
        last_digit_of_sum = sum_digit % 10
        carry_forward = sum_digit // 10
        #print(first_digit, second_digit, last_digit_of_sum)
        results.append(last_digit_of_sum)
        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None
    nextNode = None
    for i in range(len(results)-1, -1, -1):
        resultNode = ListNode(results[i], nextNode)
        nextNode = resultNode
    return resultNode


num1_list = [9,9,9,9,9,9,9]
num2_list = [9,9,9,9]
nextNode = None
for i in range(len(num1_list)-1, -1, -1):
    l1 = ListNode(num1_list[i], nextNode)
    nextNode = l1
nextNode = None
for i in range(len(num2_list)-1, -1, -1):
    l2 = ListNode(num2_list[i], nextNode)
    nextNode = l2
print('Number 1:', end=" ")
printLinkedList(l1)
print('Number 2:', end=" ")
printLinkedList(l2)
result_list = addTwoNumbers(l1, l2)
print('Sum:', end=" ")
printLinkedList(result_list)