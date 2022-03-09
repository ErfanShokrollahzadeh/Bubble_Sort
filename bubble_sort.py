import random

def bubble_sort(element):
    n = len(element)
    for n in range(len(element) -1, 0, -1):
        for i in range(n):
            if element[i] > element[i + 1]:
                element[i], element[i + 1] = element[i + 1], element[i]
elements=[]
n=10
for i in range(n):
    elements.append(random.randint(1,21))

print("Unsorted list is,")
print(elements)
bubble_sort(elements)
print("Sorted Array is, ")
print(elements)