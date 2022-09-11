class MyQueue:

    def __init__(self):
        self.l1=[]
        self.l2=[]
        self.c=0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.l1.append(x)
        self.l2=self.l1[self.c:]
        self.l2.reverse()
        print(self.l1,self.l2)

    def pop(self):
        """
        :rtype: int
        """
        self.c+=1
        return self.l2.pop()
        
        

    def peek(self):
        """
        :rtype: int
        """
        return self.l2[len(self.l2)-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.l2)==0:
            return True
        return False
        



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()