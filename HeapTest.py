import heapq

l = [2,7,4,1,8,1]
print(l)

heap = heapq.heapify(l)
print(l)

print(heapq.nlargest(2,l))

print(len(l))

