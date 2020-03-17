#https://app.codesignal.com/interview-practice/task/HmNvEkfFShPhREMn4

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    prev = None
    current = l 
    while(current is not None): 
        next = current.next
        current.next = prev 
        prev = current 
        current = next
        head = prev
    return l == head

        