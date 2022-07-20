from collections import deque
def main():
    print('welcome to queue playground')
    queue = deque([1])
    queue.append(2)
    print(queue)
    a=queue.pop()
    print(queue)
    
if __name__ == "__main__":
  main()