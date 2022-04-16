class SimpleQueue:
    maxsize = 10
    def __init__(self):
        self.head = 0
        self.tail = self.head

        self.body = [None]*self.maxsize

    def queue(self,val):
        self.body[self.tail]=val
        self.tail = self.tail +1
        if self.tail == self.maxsize:
            self.tail = 0
        return self

    def dequeue(self):
        if self.head == self.tail and self.body[self.tail] == None:
            return None
        retleved_value = self.body[self.head]
        self.body[self.head] = None
        self.head = self.head+1
        if self.head == self.maxsize:
            self.head = 0
        return retleved_value

    def print_queue(self):
        print(f"head{self.head}")
        print(f"tail{self.tail}")
        print(self.body)



q = SimpleQueue()
for i in range(5):
  q.queue(i)
  q.print_queue()
q.dequeue()
q .print_queue()
q.dequeue()
q .print_queue()
q.dequeue()
q .print_queue()
q.queue(100)
q.print_queue()
q.queue(101)
q.print_queue()
q.queue(102)
q.print_queue()
q.queue(103)
q.print_queue()
q.dequeue(),q.dequeue(),q.dequeue()
q.print_queue()
q.dequeue(),q.dequeue(),q.dequeue()
q.print_queue()
