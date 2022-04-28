import sys

sys.path.append('queues//')
from data_structures.queue import Queue


def q2():
    queue1 = Queue()
    print(queue1)
    queue1.enqueue(3)
    print(queue1)
    queue1.enqueue(5)
    print(queue1)
    queue1.dequeue()
    print(queue1)
    queue1.enqueue(7)
    print(queue1)
    queue1.peek()
    print(queue1)
    queue1.enqueue(9)
    print(queue1)
    queue1.dequeue()
    print(queue1)


def main():
    q2()


if __name__ == '__main__':
    main()
