## 1
### What does each queue operation do?
`size` or `len`: returns the number of items in the queue \
`push`: adds an item to the back of the queue \
`pop`: removes the front item of the queue and returns it \
`is_empty`: returns True if the queue is empty else False \
`peek`: returns the front item of the queue without modifying the queue

## 2
### What are the contents of the queue after the following operations are completed?
| Code                | Result  |
|---------------------|---------|
| `queue1 = Queue()`  | []      |
| `queue1.enqueue(3)` | [3]     |
| `queue1.enqueue(5)` | [5,3]   |
| `queue1.dequeue()`  | [5]     |
| `queue1.enqueue(7)` | [7,5]   |
| `queue1.peek()`     | [7,5]   |
| `queue1.enqueue(9)` | [9,7,5] |
| `queue1.dequeue()`  | [9,7]   |

The final contents of the queue are [9,7]

## 3
### Give an example of a queue in a real life situation.
A queue can represent waiting in line at a store.

## 4
### Describe an algorithm for reversing a list using a queue.
Since 1,2,3,4 are always added first to last in that order, no matter where four dequeue operations
are placed within the code (given that the queue exists and isn't empty), They must always leave in that
order.