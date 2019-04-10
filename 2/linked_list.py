class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Linked_list:
    def __init__(self,head = None):
        self.head = head
        self.size = 0

    def delete_element(self,value):
        elements = self.find_element(value)
        if elements[1] is not None:
            elements[0].next = elements[1].next
        else:
            elements[0].next = None
        self.size -= 1
        del(elements[1])

    def getLastTwoElements(self):
        current = self.head
        current = self.head

        while current.next is not None:
            previous = current
            current = current.next

        return [previous,current]

    def delete_list(self):
        while self.size:
            if self.size >= 2:
                elements = self.getLastTwoElements()
                elements[0].next = None
                del elements[1]
                self.size -= 1
            else:
                self.head = None
                self.size -= 1

    def delete_list_garbageCollector(self):
        self.head = None
        current = self.head
        if current is not None:
            while current.next is not None:
                tmp = current
                del current
                current = tmp.next
                self.size -= 1 

    def find_element(self,value):
        current = self.head
        previous = None
        while current.value != value:
            previous = current
            if current.next is not None:
                current = current.next
            else:
                break

        return [previous,current]

    def print_list(self):
        current = self.head
        tab = []
        if current is not None:
            while current.next is not None:
                tab.append(current.value)
                current = current.next

        print("tab: ")
        print(tab)

    def insert(self,previous,nextNode,x):
        previous.next = x
        x.next = nextNode
        self.size += 1


    def add_element(self,x):
        if(self.size == 0):
            self.head = Node(x)
            self.size += 1
        else:
            current = self.head
            previous = None
            while(True):
                if current is None:
                    current = Node(x)
                    previous.next = current
                    break


                if current.value > x:
                    if previous is None:
                        #current is head
                        tmp = self.head
                        self.head = Node(x)
                        self.head.next = tmp
                    else:
                        self.insert(previous,current,Node(x))

                    break
                else:
                    previous = current
                    current = current.next
                    

