from FibonacciHeapD.FibonacciHeap import FibonacciHeap
from FibonacciHeapD.Node import node

fh = FibonacciHeap()
fh.Fib_Heap_Insert(node(2))
fh.Fib_Heap_Insert(node(7))
fh.Fib_Heap_Insert(node(6))
fh.Fib_Heap_Insert(node(11))
fh.Fib_Heap_Insert(node(9))
print(fh.min.key)
fh.Fib_Heap_Extract_Min()
print(fh.min.key)