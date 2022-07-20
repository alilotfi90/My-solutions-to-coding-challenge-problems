class queue():
  def __init__(self,size):
    self.queue=[]
    self.size=size
  def isempty(self):
    return self.queue==[]
  def isfull(self):
    return len(self.queue)==self.size
  def enqueue(self,val):
    if not self.isfull():
      self.queue.insert(0,val)
    else:
      print('queue is full')
  def dequeue(self):
    self.queue.pop()
  def peek(self):
    if not self.isempty():
      return self.queue[-1]
    else:
      print('queue is empty')

def main():
    print('welcome to queue playground')
    q=queue(1)
    print(q.queue)
    print(q.isempty())
    print(q.isfull())
    q.enqueue(1)
    print(q.queue)
    q.dequeue()
    print(q.queue)
    q.peek()
if __name__ == "__main__":
  main()