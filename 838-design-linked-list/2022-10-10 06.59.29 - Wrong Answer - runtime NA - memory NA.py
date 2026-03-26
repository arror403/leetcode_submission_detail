class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = self.head  # Initialise temp
        count = 0  # Index of current node
 
        # Loop while end of linked list is not reached
        while (current):
            if (count == index):
                return current.data
            count += 1
            current = current.next
 
        return -1

    def addAtHead(self, new_data: int) -> None:
        # 1 & 2: Allocate the Node &
        #     Put in the data
        new_node = Node(new_data)
 
        # 3. Make next of new Node as head
        new_node.next = self.head
 
        # 4. Move the head to point to new Node
        self.head = new_node     

    def addAtTail(self, data: int) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n= n.next
        n.next = new_node

    def addAtIndex(self, index: int, data: int) -> None:
        # if not (0 <= index <= self.len):
        #     return
        # node = self.getNode(index)
        # new_node = Node(val=val, next=node, prev=node.prev)
        # node.prev.next = new_node
        # node.prev = new_node
        # self.len += 1
        if index == 0:
            self.addAtHead(data)
            return

        if index == self.get_count():
            self.addAtTail(data)
            return

        i = 1
        n = self.head
        while i < index-1 and n is not None:
            n = n.next
            i = i+1
        if n is None:
            print("Index out of bound")
            return
        else: 
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node             

    def deleteAtIndex(self, position: int) -> None:
        # If linked list is empty
        if self.head == None:
            return
 
        # Store head node
        temp = self.head
 
        # If head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return
 
        # Find previous node of the node to be deleted
        for i in range(position -1 ):
            temp = temp.next
            if temp is None:
                break
 
        # If position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return
 
        # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        next = temp.next.next
 
        # Unlink the node from linked list
        temp.next = None
        temp.next = next

    def get_count(self):
        if self.head is None:
            return 0
        n = self.head
        count = 0
        while n is not None:
            count = count + 1
            n = n.next
        return count
        
    def printList(head):
        while (head != None):       
            print(' ' + str(head.data), end = '')
            head = head.nextNode;    
        print()
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)