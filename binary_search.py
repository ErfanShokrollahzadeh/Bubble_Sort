import random

def bubble_sort(element):
    n = len(element)
    for n in range(len(element) - 1, 0, -1):
        for i in range(n):
            if element[i] > element[i + 1]:
                element[i], element[i + 1] = element[i + 1], element[i]

def binary_search(elements,variable,start,mid,end):
    if start == mid == end:
        if elements[mid] == variable:
            return print(f"variable = {variable} is exists")
        else:
            return print(f"variable = {variable} not exists")

    elif elements[mid] > variable:
        return binary_search(elements, variable,start, int((start + mid-1)/2) , mid-1)
    elif elements[mid] < variable:
        return binary_search(elements, variable, mid +1, int((mid+1 + end)/2), end)

elements=[]
n=10
for i in range(n):
    elements.append(random.randint(1,21))

print(elements)
bubble_sort(elements)
print(f"Sorted Array is: {elements}")
print("now you can search your choice gusse 👇")
variable = int(input("Enter your element guss: "))
binary_search(elements,variable,0, int((0 + len(elements) - 1) / 2) , len(elements) - 1)
print(elements)