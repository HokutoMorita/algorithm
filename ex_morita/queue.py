from typing import Any


class Queue(object):

    def __init__(self) -> None:
        self.queue = []
    
    def enqueue(self, data: Any) -> None:
        self.queue.append(data)
    
    def dequeue(self) -> Any:
        if self.queue: # queueがNoneではない場合
            return self.queue.pop(0) # リストの先頭の要素を取り出す

if __name__=='__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue.queue)
    queue.dequeue()
    print(queue.queue)
