class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Head:
    def __init__(self):
        self.head=None
if __name__ == "__main__":
    linked_list=Head()
    
    linked_list.head=Node(1)
    second=Node(2)
    third=Node(3)
    fourth=Node(4)
    
    linked_list.head.next=second
    second.next=third
    third.next=fourth
    
    while(linked_list.head!=None):
        print(linked_list.head.value)
        linked_list.head=linked_list.head.next
    
