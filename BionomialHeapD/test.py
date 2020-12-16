from BionomialHeapD.BinomialHeap import BinomialHeap
import networkx as nx

def createGraph():
    G = nx.DiGraph()

bh = BinomialHeap()
nums = [7, 2, 8, 11, 9, 23, 14, 16, 18, 15]
for x in nums:
    bh.insert(x)
print(bh)