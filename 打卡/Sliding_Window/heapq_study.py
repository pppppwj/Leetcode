# 学习heapq的一些内部实现

# min heap :: parent <= children


def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    while pos > startpos:
        # parent :: i
        # left child :: 2*i + 1, right child :: 2*i + 2
        # child to parent :: (child - 1) // 2 ( //2 which can use >> )
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:  # swap newitem and parent
            heap[pos] = parent
            pos = parentpos  # dont need to assign new value here
            continue
        break
    heap[pos] = newitem

def heappush(heap, item):
    heap.append(item)
    _siftdown(heap,0,len(heap)-1)



def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    childpos = 2 * pos + 1  # left child
    while childpos < endpos:
        rightpos = childpos + 1  # right child
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2 * pos + 1
    heap[pos] = newitem
    _siftdown(heap, startpos, pos) # pay attention to here!!!

def heappop(heap):
    """ Pop the samllest item off the heap, maintaining the heap invariant"""
    lastelt = heap.pop()  # raise appropriate IndexErr if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap,0)
        return returnitem
    return lastelt
